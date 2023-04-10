from __future__ import annotations

from collections import deque
from logging import Logger
from typing import Any
from typing import Dict
from typing import Iterable
from typing import List
from typing import Optional
from uuid import UUID

import pymongo
from bson.binary import UuidRepresentation
from bson.codec_options import CodecOptions
from dramatiq import Middleware
from dramatiq.broker import Broker
from dramatiq.broker import Consumer
from dramatiq.broker import MessageProxy
from dramatiq.common import current_millis
from dramatiq.logging import get_logger
from dramatiq.message import Message
from pymongo.collection import Collection
from pymongo.database import Database

from dramatiq_mongodb.state import State


class MongoDBBroker(Broker):
    """A broker that can be used with MongoDB."""

    def __init__(
        self: MongoDBBroker,
        *,
        database: Database[Any],
        collection_prefix: Optional[str] = "",
        middleware: Optional[List[Middleware]] = None,
    ) -> None:
        """Initialize a new MongoDB Broker.

        Args:
            database (Database): The database to create collections in
            collection_prefix (str, optional): Prefix for all newly created collections. Defaults to "".
            middleware (Optional[List[Middleware]], optional): Middlware to pass to Dramatiq. Defaults to None.
        """
        super().__init__(middleware=middleware)  # type: ignore

        self.logger: Logger = get_logger(__name__, type(self))  # type: ignore
        self.database = database

        self._collection_prefix = ""

        if collection_prefix:
            self._collection_prefix = collection_prefix.rstrip("_") + "_"

        self.queues: Dict[str, Collection[Any]] = {}

    def close(self) -> None:
        """Close database connection when closed by consumer."""
        self.database.client.close()

    def consume(
        self: MongoDBBroker,
        queue_name: str,
        prefetch: Optional[int] = 1,
        timeout: Optional[int] = 30000,
    ) -> Consumer:
        """Return an iterable of tasks ready to consumption.

        Args:
            queue_name (str): Name of queue to pull tasks from.
            prefetch (int, optional): Number of tasks to pull from queue at a time. Defaults to 1.
            timeout (int, optional): Number of milliseconds to query for tasks. Defaults to 30000.

        Returns:
            Consumer: An iterable containing available tasks.
        """
        return _MongoDBConsumer(self, self.queues[queue_name], prefetch, timeout)

    def declare_queue(self: MongoDBBroker, queue_name: str) -> None:
        """Create a new queue as a MongoDB collection.

        Args:
            queue_name (str): Name of queue to pull tasks from.
        """
        if queue_name not in self.queues:
            collection_name = self._collection_prefix + queue_name
            self.logger.debug(f"Creating queue ({queue_name}) which will have a collection name of {collection_name}")
            self.emit_before("declare_queue", queue_name)  # type: ignore
            std_opts = CodecOptions[Any](uuid_representation=UuidRepresentation.STANDARD)
            self.queues[queue_name] = self.database.get_collection(collection_name, codec_options=std_opts)
            self.emit_after("declare_queue", queue_name)  # type: ignore

    def enqueue(self: MongoDBBroker, message: Message[Any], *, delay: Optional[int] = None) -> Message[Any]:
        """Enqueue a new message on the designated queue.

        Args:
            message (Message[Any]): The message to enqueue
            delay (Optional[int], optional): Milliseconds until message should br processed. Defaults to None.

        Returns:
            Message[Any]: The message that was enqueued.
        """
        self.emit_before("enqueue", message, delay)  # type: ignore
        queue_name = message.queue_name
        self.logger.debug(f"Enqueueing message {message.message_id} on queue {queue_name}")
        if delay:
            millis: int = current_millis()  # type: ignore
            message = message.copy(options={"eta": millis + delay})

        document = {"msg": message.asdict(), "state": State.QUEUED}
        collection = self.queues[queue_name]
        results = collection.replace_one(
            filter={"_id": UUID(message.message_id)},
            replacement=document,
            upsert=True,
        )
        if results.matched_count != 1 or results.modified_count != 1:
            self.logger.exception(f"Failed to enqueue {message.message_id}")
        self.emit_after("enqueue", message, delay)  # type: ignore
        return message

    def flush(self: MongoDBBroker, queue_name: str) -> None:
        """Drop collection that the queue resides in.

        Args:
            queue_name (str): name of the collection to drop.
        """
        queue = self.queues[queue_name]
        queue.drop()

    def flush_all(self: MongoDBBroker) -> None:
        """Drop all collections in the database that hold queues."""
        for queue_name in self.queues.keys():
            self.flush(queue_name)

    def get_declared_queues(self: MongoDBBroker) -> Iterable[str]:
        """Get a list of all queues declared in on the broker.

        Returns:
            Iterable[str]: List of all queues on the broker.
        """
        return set(self.queues.keys())


class _MongoDBConsumer(Consumer):
    def __init__(
        self: _MongoDBConsumer,
        broker: MongoDBBroker,
        queue: Collection[Any],
        prefetch: Optional[int],
        timeout: Optional[int],
    ) -> None:
        """Consumer Class that wraps around the mongodb collection used as a queue.

        Args:
            broker (MongoDBBroker): The broker this consumer is attached to.
            queue (Collection): The queue to consume messages from.
            prefetch (Optional[int]): Not currently used.
            timeout (Optional[int]): Not currently used.
        """
        self.logger: Logger = get_logger(__name__, type(self))  # type: ignore
        self.broker = broker
        self.queue: Collection[Any] = queue
        self.messages: deque[Message[Any]] = deque()
        self.prefetch = prefetch
        self.timeout = timeout

    def __next__(self: _MongoDBConsumer) -> Optional[MessageProxy]:
        """Next item in the queue to be processed.

        Returns:
            Optional[MessageProxy]: The next item to be consumed
        """
        document = self.queue.find_one_and_update(
            filter={
                "state": State.QUEUED,
            },
            update={"$set": {"state": State.CONSUMED}},
            sort=[("timestamp", pymongo.ASCENDING)],
        )
        try:
            if document:
                return MessageProxy(Message[Any](**document["msg"]))  # type: ignore
            return None
        except Exception as e:
            self.logger.exception(f"Failed to decode message: {document}. Error is: {e}")
            return None

    def ack(self: _MongoDBConsumer, message: MessageProxy) -> None:
        """Acknowledge a message as being processed.

        Args:
            message (MessageProxy): The message to ack.
        """
        results = self.queue.update_one(
            filter={"_id": UUID(message.message_id), "state": State.CONSUMED},
            update={"$set": {"state": State.DONE}},
        )

        if results.matched_count != 1 or results.modified_count != 1:
            self.logger.exception(f"Failed to ack {message.message_id}")

    def nack(self: _MongoDBConsumer, message: MessageProxy) -> None:
        """Non-Acknowledge a message as having been rejected.

        Args:
            message (MessageProxy): The message to nack.
        """
        results = self.queue.update_one(
            filter={"_id": UUID(message.message_id), "state": State.CONSUMED},
            update={"$set": {"state": State.REJECTED}},
        )

        if results.matched_count != 1 or results.modified_count != 1:
            self.logger.exception(f"Failed to nack {message.message_id}")

    def requeue(self: _MongoDBConsumer, messages: List[MessageProxy]) -> None:
        """Requeue all messaged that have been claimed but not acked or nacked.

        Args:
            messages (List[MessageProxy]): The list of messages to requeue.
        """
        for message in messages:
            self.broker.enqueue(message._message)  # noqa: SF01

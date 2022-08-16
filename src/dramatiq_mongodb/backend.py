from __future__ import annotations

import time
from typing import Any
from typing import Dict
from typing import Optional
from typing import Tuple
from uuid import UUID

from bson.binary import UuidRepresentation
from bson.codec_options import CodecOptions
from dramatiq.common import compute_backoff
from dramatiq.encoder import Encoder
from dramatiq.logging import get_logger
from dramatiq.message import Message
from dramatiq.results import ResultBackend
from dramatiq.results import ResultMissing
from dramatiq.results import ResultTimeout
from dramatiq.results.result import wrap_exception
from dramatiq.results.result import wrap_result
from pymongo.collection import Collection
from pymongo.database import Database

from dramatiq_mongodb.state import State

#: The default timeout for blocking get operations in milliseconds.
DEFAULT_TIMEOUT = 10000

#: The minimum amount of time in ms to wait between polls.
BACKOFF_FACTOR = 100


class MongoDBBackend(ResultBackend):  # type: ignore
    """Results Backend for MongoDB."""

    def __init__(
        self: MongoDBBackend,
        *,
        database: Database[Any],
        collection_prefix: Optional[str] = "",
        namespace: Optional[str] = None,
        encoder: Optional[Encoder] = None,
    ) -> None:
        """Initialize Results Backend.

        Args:
            database (Database): The database to create collections in
            collection_prefix (str, optional): Prefix for all newly created collections. Defaults to "".
            namespace (str, optional): Unused by MongoDBBackend. Defaults to "dramatiq-results".
            encoder (Encoder, optional): Unused by MongoDBBackend. Defaults to None.
        """
        if not namespace:
            namespace = "dramatiq-results"

        super().__init__(namespace=namespace, encoder=encoder)

        if collection_prefix:
            collection_prefix = collection_prefix.rstrip("_") + "_"

        self._collection_prefix = collection_prefix

        self.logger = get_logger(__name__, type(self))
        self.database = database

    def build_message_key(self: MongoDBBackend, message: Message) -> Tuple[Collection[Any], UUID]:
        """Extract the MongoDB Collection name and UUID used for documents from messae.

        Args:
            message (Message): The message with which to extract information from.

        Returns:
            Tuple[Collection, UUID]: MongoDB Collection and UUID of document in it.
        """
        return (
            self.get_collection(message),
            UUID(message.message_id),
        )

    def get_collection(self: MongoDBBackend, message: Message) -> Collection[Any]:
        """Return handle to collection based on metadata in message.

        Args:
            message (Message): Message containing queue name.

        Returns:
            Collection: Collection handle to use for results.
        """
        std_opts = CodecOptions(uuid_representation=UuidRepresentation.STANDARD)  # type: ignore
        return self.database.get_collection(self._collection_prefix + message.queue_name, codec_options=std_opts)

    def get_result(
        self: MongoDBBackend,
        message: Message,
        *,
        block: Optional[bool] = False,
        timeout: Optional[int] = None,
    ) -> Dict[Any, Any]:
        """Return results from a task.

        Args:
            message (Message): The message to retrieve results for.
            block (bool, optional): Block process flow until result is available. Defaults to False.
            timeout (int, optional): Milliseconds to wait for a result to become available. Defaults to None.

        Raises:
            ResultTimeout: No result was available within timeout period.
            ResultMissing: No result was found.

        Returns:
            Result:
        """
        if timeout is None:
            timeout = DEFAULT_TIMEOUT

        end_time = time.monotonic() + timeout / 1000
        collection, message_key = self.build_message_key(message)
        attempts = 0

        while True:
            attempts, delay = compute_backoff(attempts, factor=BACKOFF_FACTOR)
            delay /= 1000
            time_expired = time.monotonic() + delay > end_time

            document = collection.find_one(filter={"_id": message_key, "state": State.DONE})

            if document:
                result: Dict[Any, Any] = self.unwrap_result(document["result"])
                return result

            elif not block:
                raise ResultMissing(message)

            elif time_expired:
                raise ResultTimeout(message)

            time.sleep(delay)

    def store_result(self: MongoDBBackend, message: Message, result: Dict[Any, Any], ttl: Optional[int]) -> None:
        """Store result for a successful message.

        Args:
            message (Message): Message to store results for.
            result (Result): Result of successful processing.
            ttl (int): Not currently used.
        """
        ttl = ttl  # Ugly hack to get argument checker to let me leave this in.
        collection, message_key = self.build_message_key(message)
        collection.update_one(
            filter={"_id": message_key},
            update={"$set": {"result": wrap_result(result)}},
        )

    def store_exception(self: MongoDBBackend, message: Message, exception: Exception, ttl: Optional[int]) -> None:
        """Store result for a failed message as a serialized exception.

        Args:
            message (Message): Message to store results for.
            exception (Exception): Exception during processing.
            ttl (int): Not currently used.
        """
        ttl = ttl  # Ugly hack to get argument checker to let me leave this in.
        collection, message_key = self.build_message_key(message)
        collection.update_one(
            filter={"_id": message_key},
            update={"$set": {"exception": wrap_exception(exception)}},
        )

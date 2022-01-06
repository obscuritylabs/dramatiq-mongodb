from enum import Enum


class State(str, Enum):
    """Enum of possible task states."""

    QUEUED = "QUEUED"
    CONSUMED = "CONSUMED"
    DONE = "DONE"
    REJECTED = "REJECTED"

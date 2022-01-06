from typing import Any
from typing import Dict
from typing import TypeAlias
from typing import Union

Result: TypeAlias = Dict[Any, Any]
Missing: TypeAlias = None
MResult: TypeAlias = Union[Result, Missing]

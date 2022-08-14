from typing import Iterator

# We can only import Protocol if TYPE_CHECKING (see import site of this module)
# because it's a development dependency, and is not available at runtime.
from typing_extensions import Protocol


class HasGettableStringKeys(Protocol):
    def keys(self) -> Iterator[str]:
        ...

    def __getitem__(self, key: str) -> str:
        ...

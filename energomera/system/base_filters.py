import attr

from typing import (
    Any,
    Optional,
    Callable,
    Dict,
    List,
    Tuple,
    Union,
    Type,
)


class BaseFilter:
    @property
    def key(self) -> Tuple[int]:
        raise NotImplementedError()

    def check(self, data: Any) -> bool:
        raise NotImplementedError()

    def extract_data(self, data: Any) -> Any:
        raise NotImplementedError()

    def __eq__(self, other):
        return hash(self) == hash(other)

    def __hash__(self) -> int:
        return hash(self.key)

    def __repr__(self) -> str:
        return f'<BaseFilter key={self.key}>'


@attr.attrs(repr=False, hash=False, eq=False)
class ByteFilter(BaseFilter):
    cmd = attr.attrib(type=Union[None, int, bytes, List[int], Tuple[int]], default=None)

    @property
    def key(self) -> Tuple[int]:
        if self.cmd is None:
            raise TypeError('\'NoneType\' object cannot be a key')
        if type(self.cmd) is int:
            return self.cmd,
        return tuple(self.cmd)

    def check(self, data: Any) -> bool:
        if len(self.key) > len(data):
            return False
        return self.key == tuple(data[:len(self.key)])

    def extract_data(self, data: Any) -> Any:
        if len(self.key) > len(data):
            return None
        return data[len(self.key):]

    def __repr__(self) -> str:
        return f'<ByteFilter key={self.key}>'

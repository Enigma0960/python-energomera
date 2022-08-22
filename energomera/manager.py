#
# class Group:
#     def __init__(self, cmd: Union[int, List[int]]):
#         self._cmd = cmd if type(cmd) is List[int] else [cmd]
#
#     @property
#     def cmd(self) -> List[int]:
#         return self._cmd
#
#     def __call__(self, cmd: List[int]):
#         return self._cmd + cmd
#
#
# TreeType = Dict[Tuple[int], List[Callable]]
#
#
# class Tree:
#     def __init__(self):
#         self._tree: TreeType = {}
#         self._deep: int = 0
#
#     def add(self, cmd: List[int], callback: Callable) -> None:
#         key = tuple(cmd)
#         self._deep = max(self._deep, len(cmd))
#         if key not in self._tree:
#             self._tree[key] = [callback]
#         else:
#             self._tree[key].append(callback)
#
#     def remove(self, callback: Callable):
#         _temp = self._tree.copy()
#         for key, value in _temp.items():
#             if callback in value:
#                 self._tree[key].remove(callback)
#                 if len(self._tree[key]) == 0:
#                     del self._tree[key]
#
#     def call(self, data: List[int]) -> None:
#         for index in range(self._deep, 0, -1):
#             key = tuple(data[:index])
#             if key in self._tree:
#                 data = data[index:]
#                 for call in self._tree[key]:
#                     call(data)
#                 return
#
#
# class Manager:
#     def __init__(self, protocol):
#         self._tree: Tree = Tree()
#
#     def _register_handler(self, cmd_list: List[int], callback: Callable) -> None:
#         self._tree.add(cmd=cmd_list, callback=callback)
#
#     def handler(self, cmd: Union[int, List[int], Group]):
#         def decorator(callback):
#             if type(cmd) is list:
#                 self._register_handler(cmd_list=cmd, callback=callback)
#             elif type(cmd) is Group:
#                 self._register_handler(cmd_list=cmd.cmd, callback=callback)
#             else:
#                 self._register_handler(cmd_list=[cmd], callback=callback)
#             return callback
#
#         return decorator
#
#     def sender(self, cmd: Union[int, List[int], Group]):
#         def decorator(callback):
#             pass
#
#         return decorator

import asyncio

from typing import (
    Any,
    Optional,
    Callable,
    Union,
    List,
)


def callback(func: Callable[..., Any]) -> Callable[..., Any]:
    setattr(func, '__callback__', True)
    return func


def is_callback(func: Callable[..., Any]) -> bool:
    return getattr(func, '__callback__', False) is True


class BaseInterface:
    def __init__(self):
        pass

    async def read(self) -> bytes:
        raise NotImplementedError()

    async def write(self, data: bytes) -> None:
        raise NotImplementedError()


class BasePacket:
    def __init__(self):
        pass


class BaseProtocol:
    def __init__(self, interface: BaseInterface):
        self._interface = interface

    @property
    def interface(self) -> BaseInterface:
        return self._interface


class CmdFilter:
    pass


class Manager:
    def __init__(self, protocol: BaseProtocol):
        pass

    def register_handler(self, function: Callable[..., Any], filters: Optional[CmdFilter] = None) -> None:
        pass

    def register_sender(self, function: Callable[..., Any], filters: Optional[CmdFilter] = None) -> None:
        pass

    def handler(self, filters: Optional[CmdFilter] = None):
        def decorator(function: Callable[..., Any]):
            self.register_handler(function=function, filters=filters)
            return function

        return decorator

    def sender(self, filters: Optional[CmdFilter] = None):
        def decorator(function: Callable[..., Any]):
            return self.register_sender(function=function, filters=filters)

        return decorator


# test!
async def main():
    pass


if __name__ == '__main__':
    asyncio.run(main(), debug=True)

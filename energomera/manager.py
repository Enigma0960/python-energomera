from typing import Union, List, Dict, Tuple, Callable


class Group:
    def __init__(self, cmd: Union[int, List[int]]):
        self._cmd = cmd if type(cmd) is List[int] else [cmd]

    @property
    def cmd(self) -> List[int]:
        return self._cmd

    def __call__(self, cmd: List[int]):
        return self._cmd + cmd


TreeType = Dict[Tuple[int], List[Callable]]


class Tree:
    def __init__(self):
        self._tree: TreeType = {}
        self._deep: int = 0

    def add(self, cmd: List[int], callback: Callable) -> None:
        key = tuple(cmd)
        self._deep = max(self._deep, len(cmd))
        if key not in self._tree:
            self._tree[key] = [callback]
        else:
            self._tree[key].append(callback)

    def remove(self, callback: Callable):
        _temp = self._tree.copy()
        for key, value in _temp.items():
            if callback in value:
                self._tree[key].remove(callback)
                if len(self._tree[key]) == 0:
                    del self._tree[key]

    def call(self, data: List[int]) -> None:
        for index in range(self._deep, 0, -1):
            key = tuple(data[:index])
            if key in self._tree:
                data = data[index:]
                for call in self._tree[key]:
                    call(data)
                return


class Manager:
    def __init__(self, protocol):
        self._tree: Tree = Tree()

    def _register_handler(self, cmd_list: List[int], callback: Callable) -> None:
        self._tree.add(cmd=cmd_list, callback=callback)

    def handler(self, cmd: Union[int, List[int], Group]):
        def decorator(callback):
            if type(cmd) is list:
                self._register_handler(cmd_list=cmd, callback=callback)
            elif type(cmd) is Group:
                self._register_handler(cmd_list=cmd.cmd, callback=callback)
            else:
                self._register_handler(cmd_list=[cmd], callback=callback)
            return callback

        return decorator

    def sender(self, cmd: Union[int, List[int], Group]):
        def decorator(callback):
            pass

        return decorator

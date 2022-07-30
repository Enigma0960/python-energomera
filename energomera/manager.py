from typing import Union, List, Dict, Tuple, Callable


class Group:
    pass


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
        for key, value in self._tree.items():
            if callback in value:
                self._tree[key].remove(callback)

    def call(self, data: List[int]) -> None:
        for index in range(self._deep, 0, -1):
            key = tuple(data[:index])
            if key in self._tree:
                data = data[index:]
                for call in self._tree[key]:
                    call(data)
                return


class Manager:
    def __init__(self):
        self.tree: Tree = Tree()

    def _register_handler(self, cmd_list: List[int], callback: Callable) -> None:
        self.tree.add(cmd=cmd_list, callback=callback)

    def handler(self, cmd: Union[Group, List[int]]):
        def decorator(callback):
            self._register_handler(cmd_list=cmd, callback=callback)
            return callback

        return decorator

# def sender(self, cmd_list: Union[Group, List[int]]):
#     def decorator(callback):
#         pass
#
#     return decorator

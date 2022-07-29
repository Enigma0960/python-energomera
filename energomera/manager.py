from typing import Union, List, Dict, Set, Callable


class Group:
    pass


TreeType = Dict[int, Union[Dict, Callable, List[Callable]]]


class Tree:
    def __init__(self):
        self._tree: TreeType = {}

    @staticmethod
    def _recursive_build(tree: TreeType, left: int, right: List[int], callback: Callable) -> TreeType:
        # check tail variant
        if len(right) == 0:
            if left in tree:
                if type(tree[left]) is list:
                    tree[left].append(callback)
            else:
                tree[left] = [callback]
                return tree
        return tree

    def add(self, keys: List[int], callback: Callable):
        self._tree = self._recursive_build(self._tree, keys[0], keys[1:], callback)


class Manager:
    def __init__(self):
        self.tree: Tree = Tree()

    def _register_handler(self, cmd_list: List[int], callback: Callable) -> None:
        self.tree.add(keys=cmd_list, callback=callback)

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

from typing import Union, List, Dict, Set, Callable


class Group:
    pass


TreeType = Dict[int, Union[Dict, Callable, List[Callable]]]


class Tree:
    def __init__(self):
        self._tree: TreeType = {}

    @staticmethod
    def _recursive_add(tree: TreeType, left: int, right: List[int], callback: Callable) -> TreeType:
        if left not in tree:
            if len(right) == 0:
                tree[left] = {'call': [callback]}
            else:
                tree[left] = Tree._recursive_build({}, right[0], right[1:], callback)
        else:
            if len(right) == 0:
                if 'call' not in tree[left]:
                    tree[left]['call'] = [callback]
                else:
                    tree[left]['call'].append(callback)
            else:
                tree[left] = Tree._recursive_build(tree[left], right[0], right[1:], callback)
        return tree

    def add(self, keys: List[int], callback: Callable) -> None:
        self._tree = self._recursive_build(self._tree, keys[0], keys[1:], callback)

    def call(self, data: List[int]) -> None:
        pass


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

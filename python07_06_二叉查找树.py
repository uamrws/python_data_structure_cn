"""
二叉查找树提供的接口：
Map() 创建一个新的空 map 。
put(key，val) 向 map 中添加一个新的键值对。如果键已经在 map 中，那么用新值替换
旧值。
get(key) 给定一个键，返回存储在 map 中的值，否则为 None。
del 使用 del map[key] 形式的语句从 map 中删除键值对。
len() 返回存储在映射中的键值对的数量。
in 返回 True 如果给定的键在 map 中。

"""


class BinarySearchTreeIter(object):
    def __init__(self, bst_obj):
        self.bst_obj = bst_obj

    def __iter__(self):
        try:
            return iter(self.bst_obj.root)
        except TypeError:
            return self

    def __next__(self):
        raise StopIteration


class TreeNode(object):
    def __init__(self, key, val, parent=None):
        self.key = key
        self.payload = val
        self.parent = parent
        self.left_child = None
        self.right_child = None

    def has_both_children(self):
        return all([self.left_child, self.right_child])

    def has_any_children(self):
        return any([self.left_child, self.right_child])

    def has_left_child(self):
        return self.left_child is not None

    def has_right_child(self):
        return self.right_child is not None

    def is_left_child(self):
        return not self.is_root() and self.parent.left_child == self

    def is_right_child(self):
        return not self.is_root() and self.parent.right_child == self

    def is_root(self):
        return self.parent is None

    def is_leaf(self):
        return not self.has_any_children()

    def replace(self, key, val):
        self.key = key
        self.payload = val

    def __iter__(self):
        yield self.key
        if self.left_child:
            for i in self.left_child:
                yield i
        if self.right_child:
            for i in self.right_child:
                yield i


class BinarySearchTree(object):
    def __init__(self):
        self.root = None
        self.size = 0

    def _put(self, current_node, key, val):
        if key < current_node.key:
            if current_node.left_child:
                self._put(current_node.left_child, key, val)
            else:
                current_node.left_child = TreeNode(
                    key, val, parent=current_node)
        elif key > current_node.key:
            if current_node.right_child:
                self._put(current_node.right_child, key, val)
            else:
                current_node.right_child = TreeNode(
                    key, val, parent=current_node)
        else:
            current_node.replace(key, val)
            self.size -= 1

    def put(self, key, value):
        if self.root is None:
            self.root = TreeNode(key, value)
        else:
            self._put(self.root, key, value)

    def _get(self, current_node, key):
        if current_node is None:
            raise KeyError(key)
        elif current_node.key == key:
            return current_node
        elif key < current_node.key:
            return self._get(current_node.left_child, key)
        else:
            return self._get(current_node.right_child, key)

    def get(self, key, default=None):
        try:
            return self._get(self.root, key).payload
        except KeyError:
            return default

    def delete(self, key):
        target_node = self._get(self.root, key)
        # 当有两个子分支的时候，可以从左分支中找最大的分支做后继节点，或者从右分支中找最小的分支做后继节点
        if target_node.has_both_children():
            """
            以左分支为例，后继节点有以下特征：
            1.在左分支中最大，即此节点处在左分支的最右分支且本身没有右分支
            2.此节点一定是父节点的右节点
            3.此节点的子节点一定是左节点，或者无节点
            """
            left_max_node = self.find_max(target_node.left_child)
            target_node.replace(left_max_node.key, left_max_node.payload)
            left_max_node.parent.right_child = left_max_node.left_child
        # 当目标节点不超过1个子节点时，首先判断节点是否是根节点，其余只需要判断该节点是哪种节点即可
        else:
            if target_node.is_root():
                self.root = target_node.left_child or target_node.right_child
            elif target_node.is_left_child:
                target_node.parent.left_child = target_node.left_child or target_node.right_child
            else:
                target_node.parent.right_child = target_node.left_child or target_node.right_child

    def find_max(self, current_node):
        if not current_node.has_right_child():
            return current_node
        current_node = current_node.right_child
        return self.find_max(current_node)

    def __len__(self):
        return self.size

    def __iter__(self):
        return iter(BinarySearchTreeIter(self))

    def __setitem__(self, key, value):
        self.put(key, value)
        self.size += 1

    def __getitem__(self, item):
        return self._get(self.root, item).payload

    def __delitem__(self, key):
        self.delete(key)
        self.size -= 1

    def __contains__(self, item):
        try:
            self._get(self.root, item)
            return True
        except KeyError:
            return False


if __name__ == '__main__':
    import random

    bt = BinarySearchTree()
    for i in bt:
        pass
    bt[chr(110)] = 110
    alist = [[chr(i), i] for i in range(97, 123) if i != 110]
    random.shuffle(alist)
    for key, val in alist:
        bt[key] = val
    for i in bt:
        print(i)
    bt.delete('n')
    print('-' * 20)
    for i in bt:
        print(i)

"""
如我们上一节内容，一个二叉查找树，如果顺序的去插入值，性能会降低到O(n)，
我们通过一个自动平衡的二叉查找树来使树的查找性能保持在O(logN)

平衡二叉查找树AVL的实现思路：
1.应该有一个值，始终记录左右树的高度差，我们称之为平衡因子，当左树高的时候我们加1，右树高的时候减1
2.当我们朝一个树插入数据时，会在相应的位置生成一个叶节点
3.如果生成的叶节点是其父节点的左子节点，我们应当给其父节点的平衡因子加1，反之减1
4.当父节点的值不为零时，我们应当递归的进行判断，直到根或者某一节点的平衡因子为零,
5.解释：即当一个节点的左右子树出现高度差的时候，必然意味着其父节点高度差有变化，
       而其父节点的平衡因子的增减，又取决去其是父节点的左右哪棵子树
6.当某一节点的平衡因子即高度差大于1或者小于-1时，意味着树处于不平衡的状态
7.此时我们将对节点进行旋转，以保证树的平衡

注：树的平衡因子绝对值大于1的时候，说明左右树的高度差已经大于1了
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
        self.balance = 0

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

    def rotate_left(self, node):
        """左旋转"""
        # 变量存储目标节点的右子节点
        right_child = node.right_child
        # 更新目标节点的父节点属性，根据判断替换对应分支为右子节点
        if node.is_right_child():
            node.parent.right_child = right_child
        elif node.is_left_child():
            node.parent.left_child = right_child
        # 更新右子节点的属性，替换为父节点
        right_child.parent = node.parent
        # 替换目标节点的属性，将右子节点替换为父节点
        node.parent = right_child
        # 将右子节点的左节点更新到目标的右节点属性上,
        node.right_child = right_child.left_child
        # 将右子节点的左节点的父节点更新为目标节点
        if right_child.left_child is not None:
            right_child.left_child.parent = node
        # 将右子节点的左节点替换为目标节点
        right_child.left_child = node
        if right_child.parent is None:
            self.root = right_child
        # 更新平衡因子，具体推导见Z01_AVL平衡二叉树的推导公式
        # f(NA) =f(OA) + 1 - min(f(OB)，0)
        # f(NB) = f(OB) + 1 + max(f(NA), 0)
        node.balance = node.balance + 1 - min(right_child.balance, 0)
        right_child.balance = right_child.balance + 1 + max(node.balance, 0)

    def rotate_right(self, node):
        """右旋转 与左旋类似"""
        left_child = node.left_child
        if node.is_right_child():
            node.parent.right_child = left_child
        elif node.is_left_child():
            node.parent.left_child = left_child
        left_child.parent = node.parent
        node.parent = left_child
        node.left_child = left_child.right_child
        if left_child.right_child is not None:
            left_child.right_child.parent = node
        left_child.right_child = node
        if left_child.parent is None:
            self.root = left_child
        # 更新平衡因子，具体推导见Z01_AVL平衡二叉树的推导公式
        # f(NA) =f(OA) -1-max(f(OB), 0)
        # f(NB) = f(OB) - 1+ min(f(NA)，0）
        node.balance = node.balance - 1 - max(left_child.balance, 0)
        left_child.balance = left_child.balance - 1 + min(node.balance, 0)

    # 重新平衡当前节点
    def rebalance(self, node):
        """
        节点的重新平衡应当有以下规则：
        1.当节点左重时(平衡因子大于0的时候)，进行右旋转：
            ⚠️注意：此时如果节点的左子节点是右重，应当先左旋转子节点。

        2.当节点右重时(平衡因子大于0的时候)，进行左旋转：
            ⚠️注意：此时如果节点的右子节点是左重，应当先右旋转子节点。

        """
        # 节点左重
        if node.balance > 0:
            if node.left_child is not None and node.left_child.balance < 0:
                self.rebalance(node.left_child)
            self.rotate_right(node)


        # 节点右重
        elif node.balance < 0:
            if node.right_child is not None and node.right_child.balance > 0:
                self.rebalance(node.right_child)
            self.rotate_left(node)

    # 递归检查树的左右高度差（平衡因子）
    def update_balance(self, node):
        """只有新增节点或者节点平衡因子不为零的才会传入判断"""
        # 如果树的平衡因子绝对值大于1,则说明高度差已经导致不平衡
        if abs(node.balance) > 1:
            self.rebalance(node)
        # 当递归前节点不是根节点时，才会向上
        elif node.parent is not None:
            # 通过判断当前分支
            if node.is_left_child():
                node.parent.balance += 1
            else:
                node.parent.balance -= 1
            # 如果当前节点的父节点不平衡，则将不平衡向上传递
            if node.parent.balance != 0:
                self.update_balance(node.parent)

    def _put(self, current_node, key, val):
        if key < current_node.key:
            if current_node.left_child:
                self._put(current_node.left_child, key, val)
            else:
                current_node.left_child = TreeNode(
                    key, val, parent=current_node)
                self.update_balance(current_node.left_child)
        elif key > current_node.key:
            if current_node.right_child:
                self._put(current_node.right_child, key, val)
            else:
                current_node.right_child = TreeNode(
                    key, val, parent=current_node)
                self.update_balance(current_node.right_child)
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

    def update_balance_for_del(self, node):
        """与插入相反"""
        # 如果树的平衡因子绝对值大于1,则说明高度差已经导致不平衡
        if abs(node.balance) > 1:
            self.rebalance(node)
        # 当递归前节点不是根节点时，才会向上
        elif node.parent is not None:
            # 通过判断当前分支
            if node.is_right_child():
                node.parent.balance += 1
            else:
                node.parent.balance -= 1
            if node.parent.balance == 0:
                self.update_balance_for_del(node.parent)

    def delete(self, key):
        target_node = self._get(self.root, key)
        # 当有两个子分支的时候，可以从左分支中找最大的分支做后继节点，或者从右分支中找最小的分支做后继节点
        if target_node.has_both_children():
            """
            以左分支为例，后继节点有以下特征：
            1.在左分支中最大，即此节点处在左分支的最右分支且本身没有右分支
            2.此节点一定是父节点的右节点
            3.此节点的子节点一定是左节点，或者无节点
            4.当一处移除后继节点时，一定会使得其父节点右子树高度变更，平衡因子应当+1
            """
            left_max_node = self.find_left_max(target_node.left_child)
            target_node.replace(left_max_node.key, left_max_node.payload)
            left_max_node.parent.right_child = left_max_node.left_child
            # 后继节点一定是父节点的右节点，删除后父节点平衡因子+1
            left_max_node.parent.balance += 1
            if left_max_node.parent.balance == 0:
                self.update_balance_for_del(left_max_node.parent)
        # 当目标节点不超过1个子节点时，首先判断节点是否是根节点，其余只需要判断该节点是哪种节点即可
        else:
            if target_node.is_root():
                self.root = target_node.left_child or target_node.right_child
            elif target_node.is_left_child:
                target_node.parent.left_child = target_node.left_child or target_node.right_child
                target_node.parent.balance -= 1
                if target_node.parent.balance == 0:
                    self.update_balance_for_del(target_node.parent)
            else:
                target_node.parent.right_child = target_node.left_child or target_node.right_child
                target_node.parent.balance += 1
                if target_node.parent.balance == 0:
                    self.update_balance_for_del(target_node.parent)
        self.size -= 1

    # 找寻左子树中最大的一个节点
    def find_left_max(self, current_node):
        if not current_node.has_right_child():
            return current_node
        current_node = current_node.right_child
        return self.find_left_max(current_node)

    # 找寻右子树中最大的一个节点
    def find_right_min(self, current_node):
        if not current_node.has_left_child():
            return current_node
        current_node = current_node.left_child
        return self.find_right_min(current_node)

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

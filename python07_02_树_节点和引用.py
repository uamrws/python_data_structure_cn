"""
第二种表示树的方法使用节点和引用。在这种情况下，我们将定义一个具有根值属性的类，以及左和右子树
"""""


class BinaryTree(object):
    def __init__(self, val):
        self.key = val
        self.left_child = None
        self.right_child = None

    def insert_left(self, val):
        _ = BinaryTree(val)
        if self.left_child:
            _.left_child = self.left_child
            self.left_child = _
        self.left_child = _

    def insert_right(self, val):
        _ = BinaryTree(val)
        if self.left_child:
            _.right_child = self.right_child
            self.right_child = _
        self.right_child = _

    def get_left_child(self):
        return self.left_child

    def get_right_child(self):
        return self.right_child

    def get_rootval(self):
        return self.key

    def set_rootval(self, val):
        self.key = val


if __name__ == '__main__':
    r = BinaryTree('a')
    print(r.get_rootval())
    print(r.get_left_child())
    r.insert_left('b')
    print(r.get_left_child())
    print(r.get_left_child().get_rootval())
    r.insert_right('c')
    print(r.get_right_child())
    print(r.get_right_child().get_rootval())
    r.get_right_child().set_rootval('hello')
    print(r.get_right_child().get_rootval())

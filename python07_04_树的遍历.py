"""
树的遍历有三种方式，分为：先序，中序，后序
先序	在先序遍历中，我们首先访问根节点，然后递归地做左侧子树的先序遍历，随后是右侧子树的递归先序遍历。	
中序	在一个中序遍历中，我们递归地对左子树进行一次遍历，访问根节点，最后递归遍历右子树。	
后序	在后序遍历中，我们递归地对左子树和右子树进行后序遍历，然后访问根节点。

"""""


class BinaryTree(object):
    def __init__(self, val=None):
        self.key = val
        self.leftchild = None
        self.rightchild = None

    def insert_left(self, val=None):
        _ = BinaryTree(val)
        if self.leftchild:
            _.leftchild = self.leftchild
            self.leftchild = _
        else:
            self.leftchild = _

    def insert_right(self, val=None):
        _ = BinaryTree(val)
        if self.rightchild:
            _.rightchild = self.rightchild
            self.rightchild = _
        else:
            self.rightchild = _

    def get_leftchild(self):
        return self.leftchild

    def get_rightchild(self):
        return self.rightchild

    def get_rootval(self):
        return self.key

    def set_rootval(self, val):
        self.key = val

    def pre_order(self):
        print(self.get_rootval())
        if self.get_leftchild():
            self.get_leftchild().pre_order()
        if self.get_rightchild():
            self.get_rightchild().pre_order()
# 先序遍历
def preorder(tree):
    if tree:
        print(tree.get_rootval())
        preorder(tree.get_leftchild())
        preorder(tree.get_rightchild())


# 中序遍历
def inorder(tree):
    if tree:
        inorder(tree.get_leftchild())
        print(tree.get_rootval())
        inorder(tree.get_rightchild())


# 后序遍历
def postorder(tree):
    if tree:
        postorder(tree.get_leftchild())
        postorder(tree.get_rightchild())
        print(tree.get_rootval())

if __name__ == '__main__':
    b_tree = BinaryTree(50)
    for i in range(50):
        if i % 2:
            b_tree.insert_left(i)
        else:
            b_tree.insert_right(i)
    b_tree.pre_order()

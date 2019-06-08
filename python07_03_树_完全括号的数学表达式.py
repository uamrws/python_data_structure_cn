"""
完全括号的数学表达式构建分析树
(3*(4+5))
思路：
    1.拆分表达式为列表，进行遍历，并创建一个空树
    2.当遇到左括号时，创建一个节点作为根的左节点，并下沉到左节点
    3.当遇到操作数时，给当前节点赋值，并返回上一节点，
    4.当遇到运算符时，给根节点赋值当前预算符，并下沉到右节点。
    5.当遇到右括号时，返回父节点
    6.依次重复上述过程，完成分析树

通过解析树计算结果。
思路：
    1.通过递归得出结果
"""""
from pythonds.basic.stack import Stack


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
        self.leftchild = _

    def insert_right(self, val=None):
        _ = BinaryTree(val)
        if self.leftchild:
            _.rightchild = self.rightchild
            self.rightchild = _
        self.rightchild = _

    def get_leftchild(self):
        return self.leftchild

    def get_rightchild(self):
        return self.rightchild

    def get_rootval(self):
        return self.key

    def set_rootval(self, val):
        self.key = val


def build_parse_tree(fpexp):
    fplist = fpexp.split()
    parse_tree = BinaryTree()
    current_node = parse_tree
    parent_stack = Stack()
    parent_stack.push(parse_tree)
    for i in fplist:
        if i == '(':
            current_node.insert_left()
            parent_stack.push(current_node)
            current_node = current_node.get_leftchild()
        elif i in ('+', '-', '*', '/'):
            current_node.set_rootval(i)
            parent_stack.push(current_node)
            current_node.insert_right()
            current_node = current_node.get_rightchild()
        elif i == ')':
            current_node = parent_stack.pop()
        else:
            current_node.set_rootval(i)
            current_node = parent_stack.pop()
    return parse_tree


def evaluate(parse_tree):
    left = parse_tree.get_leftchild()
    right = parse_tree.get_rightchild()
    if left is None and right is None:
        return parse_tree.get_rootval()
    return str(eval(evaluate(left)+parse_tree.get_rootval()+evaluate(right)))


if __name__ == '__main__':
    parse_tree = build_parse_tree('( ( 2 * 5 ) * ( 3 * ( 10 + 5 ) ) ) ')
    print(evaluate(parse_tree))
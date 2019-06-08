# from timeit import Timer
#
# t1 = Timer('a(500,33)', 'from python02_01_队列_约瑟夫环 import josephus as a')
# t2 = Timer('b(500,33)', 'from python02_02_扩展_约瑟夫环算法实现 import josephus as b')
#
# print(t1.timeit(number=1000))
# print(t2.timeit(number=1000))
from python07_07_平衡二叉查找树AVL import BinarySearchTree
def test_AVL():
    import random

    bt = BinarySearchTree()
    for i in bt:
        pass
    bt[chr(110)] = 110
    alist = [[chr(i), i] for i in range(97, 123) if i != 110]
    random.shuffle(alist)
    for key, val in alist:
        bt[key] = val
    assert sorted([chr(i) for i in range(97, 123)])==sorted(list(bt))

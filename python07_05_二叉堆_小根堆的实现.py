"""
二叉堆（Binary Heap)）----最小堆

Heap是一种数据结构具有以下的特点：
1）完全二叉树；（完整的二叉树是一个树，其中每个层都有其所有的节点，除了树的最底层，从左到右填充。）
2）heap中存储的值是偏序（https://zh.wikipedia.org/wiki/%E5%81%8F%E5%BA%8F%E5%85%B3%E7%B3%BB）；


二叉堆是很有趣的研究，因为堆看起来很像一棵树，但是当我们实现它时，我们只使用一个
单一的列表作为内部表示。二叉堆有两个常见的变体：最小堆（其中最小的键总是在前面）
和最大堆（其中最大的键值总是在前面）

最小堆（Min-heap）：父节点的值小于或等于子节点的值；

最大堆（Max-heap）：父节点的值大于或等于子节点的值；


完整二叉树的另一个有趣的属性是，我们可以使用单个列表来表示它。 我们不需要使用节点
和引用，甚至列表的列表。因为树是完整的，父节点的左子节点（在位置 p 处，此处的p是指下标+1）是在列表中
位置 2p 中找到的节点。 类似地，父节点的右子节点在列表中的位置 2p + 1
# 推导如下：
# 假设节点在当前第n层的p位置，其左右子节点则一定是n+1层的2p-1和2p位置，
# 可以求得节点在列表中的位置x=sum(n-1)+p，左子节点的位置y=sum(n)+p。
# sum是所有n层之前的节点数目之和，即等比数列求和公式可得，接下来的过程不细说了。

结论就是 当前节点的父节点可以通过将当前节点的索引除以 2 取整来计算
"""
import random


class BinaryHeap(object):
    def __init__(self):
        # 初始化的堆列表包含一个初始元素，方便计算
        self._heap_list = [0]
        self._size = 0

    @property
    def heap(self):
        return self._heap_list[1:]

    def build_min_heap(self, alist):
        self._heap_list.extend(alist)
        self._size += len(alist)
        # 从最后非叶节点开始比对,重构每一个节点
        current_pos = self._size // 2
        while current_pos > 0:
            self.rebuild_min_heap(current_pos)
            current_pos -= 1

    def insert(self, val):
        self._heap_list.append(val)
        self._size += 1
        # 当前插入的元素所在的位置
        current_pos = self._size
        # 循环直到当前为根节点，或者值大于父节点的值
        while current_pos // 2 > 0 and val < self._heap_list[current_pos // 2]:
            (
                self._heap_list[current_pos]
                , self._heap_list[current_pos // 2]
            ) = (
                self._heap_list[current_pos // 2]
                , self._heap_list[current_pos]
            )

            current_pos = current_pos // 2

    # 从当前节点开始，递归的向子节点重构最小堆
    def rebuild_min_heap(self, current_pos):
        # 如果当前节点*2 超出整个堆列表的范围，则说明这个节点是最后的非叶节点
        while current_pos * 2 <= self._size:
            # 对比当前节点和两个子节点，并和最小的节点比较，如果大于则互换，否则结束循环
            child_pos = self.min_child(current_pos)
            if self._heap_list[current_pos] <= self._heap_list[child_pos]:
                break
            (
                self._heap_list[current_pos]
                , self._heap_list[child_pos]
            ) = (
                self._heap_list[child_pos]
                , self._heap_list[current_pos]
            )
            current_pos = child_pos

    def min_child(self, current_pos):
        left_child_pos = current_pos * 2
        left_child_val = self._heap_list[left_child_pos]
        right_child_pos = current_pos * 2 + 1
        # 判断没有右节点的值，没有则直接返回左节点
        try:
            right_child_val = self._heap_list[right_child_pos]
        except IndexError:
            return left_child_pos
        # 返回两者最小的一个
        if left_child_val < right_child_val:
            return left_child_pos
        else:
            return right_child_pos

    def pop(self):
        # 交换根节点和最后一个节点的值
        (self._heap_list[1]
         , self._heap_list[-1]) = (self._heap_list[-1]
                                   , self._heap_list[1])
        # 获取根节点的值
        min_val = self._heap_list.pop()
        self._size -= 1
        # 重构最小堆
        self.rebuild_min_heap(1)
        return min_val


if __name__ == '__main__':
    min_heap = BinaryHeap()
    # min_heap.build_min_heap([9, 6, 5, 2, 3])
    # print(min_heap.heap)
    # min_heap.pop()
    # print(min_heap.heap)
    # min_heap.insert(1)
    # print(min_heap.heap)
    alist = []
    for i in range(1000):
        alist.append(random.randint(1, 100000))
    min_heap.build_min_heap(alist)
    print(min_heap.heap)
    print(min(alist))
    print(min_heap.pop())
    print(min_heap.heap)

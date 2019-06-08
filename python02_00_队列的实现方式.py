"""
队列抽象数据类型由以下结构和操作定义。如上所述，队列被构造为在队尾添加项的有序集合，并且从队首移除。队列保持FIFO(first in first out 先进先出)排序属性。队列操作如下:
    Queue()创建一个空的新队列。它不需要参数，并返回一个空队列。
    enqueue(item)将新项添加到队尾。它需要item作为参数，并不返回任何内容。
    dequeue()从队首移除项。它不需要参数并返回item。队列被修改。
    isEmpty()查看队列是否为空。它不需要参数，并返回布尔值。
    size()返回队列中的项数。它不需要参数，并返回一个整数。
"""""


class Queue(object):
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def is_empty(self):
        return self.items == []

    def size(self):
        return len(self.items)


queue = Queue()
queue.enqueue(10)
queue.enqueue(20)
print(queue.dequeue())
print(queue.is_empty())
print(queue.dequeue())
print(queue.is_empty())
print(queue.size())
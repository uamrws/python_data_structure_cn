"""
deque抽象数据类型由以下结构和操作定义。如上所述，deque被构造为项的有序集合，其中项从首部或尾部的任一端添加和移除。下面给出了deque操作。
    Deque()创建一个空的新deque。它不需要参数，并返回空的deque。
    addFront(item)将一个新项添加到deque的首部。它需要item参数并不返回任何内容。
    addRear(item)将一个新项添加到deque的尾部。它需要item参数并不返回任何内容。
    removeFront()从deque中删除首项。它不需要参数并返回item。deque被修改。
    removeRear()从deque中删除尾项。它不需要参数并返回item。deque被修改。
    isEmpty()测试deque是否为空。它不需要参数，并返回布尔值。
    size()返回deque中的项数。它不需要参数，并返回一个整数。
"""""


class Deque(object):
    def __init__(self):
        self.items = []

    def addFront(self, item):
        self.items.append(item)

    def removeFront(self):
        return self.items.pop()

    def addRear(self, item):
        self.items.insert(0, item)

    def removeRear(self):
        return self.items.pop(0)

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)


if __name__ == '__main__':
    deque = Deque()
    deque.addFront(10)
    deque.addFront(20)
    print(deque.removeFront())
    deque.addRear(30)
    print(deque.removeRear())
"""
无序链表的结构是项的集合，其中每个项保持相对于其他项的相对位置。下面给出了一些可能的无序链表操作。
    UnorderedList()创建一个新的空链表。它不需要参数，并返回一个空链表。
    add(item)向链表中添加一个新项。它需要item作为参数，并不返回任何内容。假定该item不在链表中。
    remove(item)从链表中删除该项。它需要item作为参数并修改链表。假设项存在于链表中。
    search(item)搜索链表中的项目。它需要item作为参数，并返回一个布尔值。
    isEmpty()检查链表是否为空。它不需要参数，并返回布尔值。
    size（）返回链表中的项数。它不需要参数，并返回一个整数。
    append(item)将一个新项添加到链表的末尾，使其成为集合中的最后一项。它需要item作为参数，并不返回任何内容。假定该项不在链表中。
    index(item)返回项在链表中的位置。它需要item作为参数并返回索引。假定该项在链表中。
    insert(pos，item)在位置pos处向链表中添加一个新项。它需要item作为参数并不返回任何内容。假设该项不在链表中，并且有足够的现有项使其有pos的位置。
    pop()删除并返回链表中的最后一个项。假设该链表至少有一个项。
    pop(pos)删除并返回位置pos处的项。它需要pos作为参数并返回项。假定该项在链表中。
"""""


# 创建节点类，存储项的值和下一个项的引用
class Node(object):
    def __init__(self, initdata):
        self._data = initdata
        self._next = None

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, next_data):
        self._next = next_data

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, new_data):
        self._data = new_data


# 创建链表
class UnorderedList(object):
    def __init__(self):
        # 链表必须有一个头部用来标识第一个项
        self.header = None

    def isEmpty(self):
        # 如果次链表无头部，说明链表中没有项
        return self.header is None

    def size(self):
        # 遍历所有取值直到节点的下一个指向为None
        items_number = 0
        current_item = self.header
        while current_item:
            items_number += 1
            current_item = current_item.next
        return items_number

    def add(self, item):
        # 向链表中添加元素，替换原头部，并将新的值替换为头部
        item = Node(item)
        item.next = self.header
        self.header = item

    def append(self, item):
        # 先链表尾部追加，首先遍历链表，取到next为空的那个项，将新项赋值
        item = Node(item)
        current_item = self.header
        while current_item.next:
            current_item = current_item.next
        current_item.next = item

    def search(self, item):
        # 查看链表中是否有值为item的这个项
        current_item = self.header
        while current_item:
            if current_item.data == item:
                return True
            current_item = current_item.next
        return False

    def remove(self, item):
        # 删除链表中值为item的项，并将这个项的后一个项赋值给前一个项的next
        pre_item = None
        current_item = self.header
        while current_item:
            next_item = current_item.next
            if current_item.data == item:
                if pre_item is None:
                    self.header = next_item
                    return
                pre_item.next = next_item
                return
            pre_item = current_item
            current_item = next_item
        # 返回-1表示链表无此项
        return -1

    def index(self, item):
        _index = -1
        current_item = self.header
        while current_item:
            _index += 1
            if current_item.data == item:
                return _index
            current_item = current_item.next
        # 无此项返回-1
        return _index

    def insert(self, pos, item):
        # 向pos下标处添加元素，需要将新项赋值给前一个项的next，并将当前项赋值给新项的next
        if pos > self.size():
            raise IndexError('out of range')
        _index = -1
        pre_item = None
        current_item = self.header
        while current_item:
            _index += 1
            if _index == pos:
                if pre_item is None:
                    self.add(item)
                    return _index
                item = Node(item)
                pre_item.next = item
                item.next = current_item
                return _index
            pre_item = current_item
            current_item = current_item.next
        return _index

    def pop(self, pos=None):
        # 删除下标为pos的项，如果没有pos删除最后的项，删除即为将后一项的赋值给前一项的next
        _index = -1
        pre_item = None
        current_item = self.header
        if pos is None:
            while current_item:
                _index += 1
                next_item = current_item.next
                if next_item is None:
                    pre_item.next = None
                    return current_item.data
                current_item = next_item
                pre_item = current_item
        elif pos > self.size():
            raise IndexError('out of range')
        else:
            while current_item:
                _index += 1
                next_item = current_item.next
                if _index == pos:
                    if pre_item is None:
                        self.header = next_item
                        return current_item
                    pre_item.next = next_item
                    return current_item.data
                current_item = next_item
                pre_item = current_item


l  = UnorderedList()
l.add(10)
print(l.size())
print(l.isEmpty())
l.add(20)
print(l.search(10))
print(l.search(11))
l.append(30)
l.append(40)
print(l.index(30))
print(l.index(40))
print(l.insert(0,50))
# print(l.insert(2,50))
# print(l.index(40))
# print(l.size())


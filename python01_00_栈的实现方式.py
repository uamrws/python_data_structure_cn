"""
栈的抽象数据类型由以下结构和操作定义。栈被构造为项的有序集合，其中项被添加和从末端移除的位置称为“顶部”。栈是有序的LIFO(last in first out 后进先出)。栈操作如下:
    Stack()创建一个空的新栈。它不需要参数，并返回一个空栈。 
    push(item)将一个新项添加到栈的顶部。它需要item做参数并不返回任何内容。 
    pop()从栈中删除顶部项。它不需要参数并返回item。栈被修改。 
    peek()从栈返回顶部项，但不会删除它。不需要参数。不修改栈。 
    isEmpty()测试栈是否为空。不需要参数，并返回布尔值。 
    size()返回栈中的item数量。不需要参数，并返回一个整数。
"""""
# 可以从pythonds模块中导入Stack类。
# from pythonds.basic.stack import Stack
#

class Stack(object):
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        return self.items.append(item)

    def peek(self):
        return self.items[-1]

    def pop(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


stack = Stack()
print(stack.is_empty())
print(stack.push(10))
print(stack.push(15))
print(stack.peek())

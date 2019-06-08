""""
一、通过栈来实现中缀表达式向后缀以及前缀表达式的转化
    简单示例：
    中缀：a+b*c
    后缀：abc*+
    前缀：+a*bc
"""""
"""
二、将中缀表达式"(A+B)*C-(D-E)*(F+G)"转换为后缀的实现：
    当我们看到如上表达式的时候，我们能够很简单的知道如何进行计算，
    每一个符号的优先级，我们都清楚的知道，但是计算机如何明确的进行计算
    则是将上述中缀表达式，转换成前缀或者后缀的形式，如何实现转化，我们实际可以通过
    栈的方式来实现
"""""
"""
A.我们首先创建一个stack用以存储所有的运算符号，并创建一个列表接受输出
B.遍历整个表达式。
    1.如果接收到的是操作数，将其置入输出列表
    2.如果接收到的是左括号，将其压入栈中，
    3.如果接收到的是右括号，则从此时的栈中弹出元素，知道弹出左括号截止，并将每一个弹出的运算符，置入输出列表
    4.如果接受到的是运算符号，则判断此符号与栈顶符号的优先级，如果栈顶的优先级高于或等于此符号，弹出栈顶的运算符号置入到输出列表，继续对比符号的优先级，直到条件不符合。
"""""
from pythonds.basic.stack import Stack


def infix_to_postfix(infix_expr):
    infix_expr = infix_expr.split()
    opers_stack = Stack()
    output = []
    prec = {
        '*': 3,
        '/': 3,
        '+': 2,
        '-': 2,
        '(': 1,
    }
    for i in infix_expr:
        if i == '(':
            opers_stack.push(i)
        elif i == ')':
            while True:
                oper = opers_stack.pop()
                if oper == '(':
                    break
                output.append(oper)
        elif i in '+-*/':
            while not opers_stack.isEmpty() and prec[opers_stack.peek()] >= prec[i]:
                output.append(opers_stack.pop())
            opers_stack.push(i)

        else:
            output.append(i)
    while not opers_stack.isEmpty():
        output.append(opers_stack.pop())
    return ''.join(output)


print(infix_to_postfix("( A + B ) * C - ( D - E ) * ( F + G )"))
print(infix_to_postfix("( A + B ) * ( C + D )"))
print(infix_to_postfix("A + B * ( C + D )"))

"""
转换成前缀的方式和之前的转换后缀方法近似，前缀是反向遍历后压栈处理
例如：
"(A+B)*C-(D-E)*(F+G)"
# GF+ED-*CBA+*-  反向遍历压栈
# -*+ABC*-DE+FG  从栈中依次取出得到前缀
"""


def infix_to_prefix(infix_expr):
    infix_expr = infix_expr.split()
    opers_stack = Stack()
    output = []
    prec = {
        '*': 3,
        '/': 3,
        '+': 2,
        '-': 2,
        ')': 1,
    }
    for i in infix_expr[::-1]:
        if i == ')':
            opers_stack.push(i)
        elif i == '(':
            while True:
                oper = opers_stack.pop()
                if oper == ')':
                    break
                output.append(oper)
        elif i in '+-*/':
            while not opers_stack.isEmpty() and prec[opers_stack.peek()] >= prec[i]:
                output.append(opers_stack.pop())
            opers_stack.push(i)

        else:
            output.append(i)
    while not opers_stack.isEmpty():
        output.append(opers_stack.pop())
    return ''.join(output[::-1])


print('*' * 40)
print(infix_to_prefix("( A + B ) * C - ( D - E ) * ( F + G )"))
print(infix_to_prefix("( A + B ) * ( C + D )"))

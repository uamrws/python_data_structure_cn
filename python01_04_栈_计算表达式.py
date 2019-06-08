from pythonds.basic.stack import Stack

"""
将中缀计算表达式转换成后缀后，通过栈就能够很好的让计算器根据运算优先级进行计算
例如：
中缀："(A+B)*C-(D-E)*(F+G)"
后缀："AB+C*DE-FG+*-"
转换为后缀后，计算机的执行实际已经是有顺序的了
"""""
"""
A.新建一个结算结果的栈
B.遍历后缀表达式
    1.如果接收到的是操作数，将操作数压入栈类
    2.如果是运算符，将栈顶的两个操作数弹出，进行相应的结算
    3.最后将结果弹出    
"""""


class Computer(object):
    def __init__(self, infix_expr):
        self.infix_expr = infix_expr.split()

    @property
    def _postfix(self):
        opers_stack = Stack()
        output = []
        prec = {
            '*': 3,
            '/': 3,
            '+': 2,
            '-': 2,
            '(': 1,
        }
        for i in self.infix_expr:
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

    def do_compute(self):
        postfix = self._postfix
        result = Stack()
        for i in postfix:
            if i in '0123456789':
                result.push(i)
            elif i in '+-*/':
                num1 = result.pop()
                num2 = result.pop()
                result.push(str(eval(num2 + i + num1)))
        return result.pop()


if __name__ == '__main__':
    computer = Computer('( 1 + 2 * 3 ) - 5 * 1 + ( 6 + 4 ) * 2')
    print(computer.do_compute())

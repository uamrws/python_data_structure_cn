""""
十进制向其他进制的转换
"""""
from pythonds.basic.stack import Stack


def base_convert(number, base):
    base_digits = '0123456789ABCDEF'
    base_stack = Stack()
    result = ''
    # 将需要转换的数字除以进制，余数为当前位的，商继续循环除以进制知道商为零
    while number:
        # 将余数作为下标在base_digits中取值，用以实现16进制
        current_number = base_digits[number % base]
        base_stack.push(current_number)
        number = number // base
    while not base_stack.isEmpty():
        result += str(base_stack.pop())
    return result

print(base_convert(10,16))
print(base_convert(10,2))
print(base_convert(10,8))

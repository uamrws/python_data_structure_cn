"""
使用递归的方式实现进制的转化
思路：
    1.一个数字num转换为进制base的字符串，
    2.conv_str(num) = conv_str(num//base)+num%base
"""""


def conv_str(num, base):
    if num < base:
        conv_base = '0123456789ABCDEF'
        return conv_base[num]
    else:
        return conv_str(num // base, base) + str(num % base)


if __name__ == '__main__':
    print(conv_str(10, 2))

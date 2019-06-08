"""
检查一个字符串的括号是否匹配
每匹配上一对括号就会在栈中移除他们，
所以判断右边括号时，当前的右边括号一定与栈顶的括号类型一致
例如：
    '{([])}'是正常的匹配，
    '{{(})}'是错误的匹配。
"""""

from pythonds.basic.stack import Stack

a = '((((((((((()))(((()())(())())))))))))))'
b = '({{[((){}[()])]}})'

st = Stack()


def match(pre, curr):
    map_dict = {'(': ')', '[': ']', '{': '}'}
    return map_dict[pre] == curr


def check(string):
    # 遍历整个字符串
    for i in string:
        # 当子串为([{其中之一时，向栈顶推入
        if i in '([{':
            st.push(i)
        # 当子串为)]}其中时，从栈顶将最近放入的起始符号抛出，如果此时栈为空，说明不匹配
        if i in ')]}':
            if st.isEmpty():
                return False
            else:
                pre = st.pop()
                # 抛出后应该判断上一个符号和当前符号是否一致，不一致说明一定不匹配
                if not match(pre, i):
                    return False
    # 当执行循环结束后，栈为空，说明字符串中的括号是匹配的，否则不匹配
    if st.isEmpty():
        return True
    else:
        return False


print(check(a))
print(check(b))

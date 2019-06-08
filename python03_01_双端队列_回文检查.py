from pythonds.basic.deque import Deque

"""
使用deque数据结构可以容易地解决经典回文问题。回文是一个字符串，读取首尾相同的字 
符，例如，radar,toot,madam。我们想构造一个算法输入一个字符串，并检查它是否是一个回文。

思路:
    1.首先创建一个双端队列，存储字符串
    2.从双端队列两端弹出数字，对数字进行比对，直到队列中的长度为1或者0，(这取决于这个回文字符串是奇数还是偶数)，如果在此期间任意一次比对不成功，则字符串不是回文字符串。
"""""

from pythonds.basic.deque import Deque
def pal_checker(string):
    deque = Deque()
    for i in string:
        deque.addFront(i)
    while deque.size() > 1:
        front = deque.removeFront()
        rear = deque.removeRear()
        if front != rear:
            return False
    return True


if __name__ == '__main__':
    print(pal_checker('toot'))
    print(pal_checker('radar'))
    print(pal_checker('asdasdsaiodfiu'))

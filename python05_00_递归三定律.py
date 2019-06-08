""""
所有递归算法必须服从三个重要的定律：
    1.	递归算法必须具有基本情况。
    2.	递归算法必须改变其状态并向基本情况靠近。
    3.	递归算法必须以递归方式调用自身。

例：计算整数列表和,用递归的方式实现列表的和
思路：
    一个整数列表的和，即为第一个元素和剩余所有元素的和即
    sum_list(num_list) = num_list[0]+sum_list(num_list[1:])
"""""

def sum_list(num_list,start = 0):
    if start>=len(num_list):
        return 0
    else:
        start+=1
        return num_list[start-1] + sum_list(num_list,start=start)


if __name__ == '__main__':
    print(sum_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10,100]))

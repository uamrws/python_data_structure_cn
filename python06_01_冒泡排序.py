"""
冒泡排序，遍历容器，通过对比相邻两个值的大小来确定，将较大值和较小值交换位置，直到将最大的值
放到容器的末尾，再遍历容器的剩余部分，重复以上操作
时间复杂度：O(n^2)
稳定性：   稳定
"""""


def bubble_sort(alist):
    for i in range(len(alist) - 1, 0, -1):
        exchange = False
        for j in range(i):
            if alist[j] > alist[j + 1]:
                alist[j], alist[j + 1] = alist[j + 1], alist[j]
                exchange = True
        # 如果排序期间没有发生过交换，说明已经是正确排序，则终止程序
        if not exchange:
            return


if __name__ == '__main__':
    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    bubble_sort(alist)
    print(alist)

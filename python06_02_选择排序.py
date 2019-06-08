"""
选择排序，在冒泡排序的基础上进行了改进，遍历时，多次比较筛选出最大值，只做一次交换，
你可能会看到选择排序与冒泡排序有相同数量的比较，因此也是O(n^2)。
然而，由于交换数量的减少，选择排序通常在基准研究中执行得更快。
"""""


def selection_sort(alist):
    for i in range(len(alist) - 1, 0, -1):
        posofmax = 0
        for j in range(1,i+1):
            if alist[j]>alist[posofmax]:
                posofmax=j
        if posofmax != i:
            alist[i],alist[posofmax]=alist[posofmax],alist[i]




if __name__ == '__main__':
    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    selection_sort(alist)
    print(alist)

"""
希尔排序，缩小增量排序法，插入排序的优化，将需要排序的列表按一定的步长增量分割成子列表进行插入排序，
例如：按照n/2的步长排序一遍，再按照n/2/2的步长排序，直到步长为1，也就是普通的插入排序

可将前面各趟的"宏观"调整看成是最后一趟的预处理，比只做一次直接插入排序效率更高。
"""""


def shell_sort(alist):
    step_size = len(alist) // 2
    while step_size >0:
        for i in range(step_size):
            for pos in range(i, len(alist), step_size):
                current_num = alist[pos]
                current_pos = pos
                while current_pos > i and alist[current_pos - step_size] > current_num:
                    alist[current_pos] = alist[current_pos - step_size]
                    current_pos -= step_size
                alist[current_pos]=current_num
        step_size //=2

if __name__ == '__main__':
    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    shell_sort(alist)
    print(alist)

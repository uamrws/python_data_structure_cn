"""
插入排序，遍历列表，从列表起始位置开始，保持一个有顺序的子列表，将当前遍历位置的元素，与子列表
最后一个元素比较，如果小于则子列表最后一个元素移动到当前遍历位置，依次类推，知道遍历位置的元素移动到0
或者有元素小于等于它
"""""


def insert_sort(alist):
    for i in range(1, len(alist)):
        current_num = alist[i]
        pos = i
        while pos > 0 and alist[pos - 1] > current_num:
            alist[pos] = alist[pos - 1]
            pos -= 1
        alist[pos] = current_num


if __name__ == '__main__':
    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    insert_sort(alist)
    print(alist)

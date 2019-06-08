"""
快速排序，快速排序的思想实际和归并排序相同，实际上也是分而治之的思路，
思路：
    1.以首个元素为枢纽值，分别在剩余列表部分的首尾放置指针，首先移动左指针，直到有元素大于枢纽值，
    停止移动，移动右指针，直到有元素小于枢纽值，交换左右指针的元素，再继续上述过程，
    直到右指针穿过左指针，即右指针的index小于左指针，此时将枢纽值与右指针的交换，
    以枢纽值为界限分割后，左边全是小于枢纽值的，右边全是大于枢纽值
    2.递归的将左右子列表快速排序，直到子列表的长度小于等于1
"""""


def quick_sort(alist, first=None, last=None):
    if first is None and last is None:
        first = 0
        last = len(alist) - 1
    if last - first <= 1:
        return
    left_mark = first
    right_mark = last
    while left_mark < right_mark:
        if alist[left_mark] < alist[first]:
            left_mark += 1
        elif alist[right_mark] > alist[first]:
            right_mark -= 1
        else:
            alist[right_mark], alist[left_mark] = alist[left_mark], alist[right_mark]
    alist[first], alist[right_mark] = alist[right_mark], alist[first]
    quick_sort(alist, first, right_mark)
    quick_sort(alist, right_mark + 1, last)


if __name__ == '__main__':
    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    quick_sort(alist)
    print(alist)

"""
归并排序，将列表不停拆分直至只有最后一个项，再将所有拆分的项排序合并
"""""


def merge_sort(alist):
    if len(alist) > 1:
        left_half = alist[:len(alist) // 2]
        right_half = alist[len(alist) // 2:]
        alist.clear()
        merge_sort(left_half)
        merge_sort(right_half)
        i = 0
        j = 0
        # 将两个列表的值遍历取出后两两对比，得到较小的项，并继续对比，直至有一个列表全部遍历完
        while i < len(left_half) and j < len(right_half):
            # 如果左列表的元素小于右列表的元素，则左列表的元素取出存入容器，并对比左列表下一个元素
            if left_half[i] < right_half[j]:
                alist.append(left_half[i])
                # 获取左列表下一个元素的下标，继续与右列表当前位置的元素比较
                i += 1
            else:
                alist.append(right_half[j])
                j += 1
        # 上述对比完成后，左右列表中，剩余的部分肯定都是大于排序好的列表中的
        if i < len(left_half):
            alist.extend(left_half[i:])
        if j < len(right_half):
            alist.extend(right_half[j:])


if __name__ == '__main__':
    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    merge_sort(alist)
    print(alist)

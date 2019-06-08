"""
在此前的文件中，我们讲述了约瑟夫环通过队列的方式实现，时间复杂度高达O(mn)，
那么约瑟夫环是否有更好地实现方式呢，答案是肯定的，数学方法的推导可以很好的解决约瑟夫环的问题。

思路：
    1.约瑟夫环的问题:从1开始报数，当报到第m个的人退出,剩下的人从1继续此过程，直到剩余一人
    2.可知，退出的人的编号一定为m%n,那么下一个人编号为m%n+1即m+1
    3.设每个人的原序号为x，当前序号为y，
        k之后的人序号可以表示为：y=x-m 即编号为n的人新编号为n-m
        k之前的人序号可以表示为：y=n+x-m 即编号为1的人新编号为 n+1-m
    4.当已知当前序号y的情况下，可以得出原序号x,
        x=(y+m-1)%n + 1
        解释：表达式原为x=(y+m)%n，但是原编号为n的人即新编号中为n-m的人取模后结果为0，
        于是将所有人的编号前移1位，取模后再后移归位，得到真正的位置编号。
    5.f(n,m) = (f(n-1,m)+m-1)%n+1，一直递归到最后只剩最后一人时即f(1,m)=1。
"""""


def josephus(n, m):
    if n == 1:
        return 1
    else:
        return (josephus(n - 1, m) + m - 1) % n + 1


if __name__ == '__main__':
    print(josephus(40, 7))

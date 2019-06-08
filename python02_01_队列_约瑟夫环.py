"""
著名的约瑟夫问题，一个一世纪著名历史学家弗拉维奥·约瑟夫斯的传奇故事。
故事讲的是，他和他的39个战友被罗马军队包围在洞中。他们决定宁愿死，也不成为罗马人的奴隶。他们围成一个圈，其中一人被指定为第一个人，顺时针报数到第七人，就将他杀死。约瑟夫斯是一个成功的数学家，他立即想出了应该坐到哪才能成为最后一人。最后，他加入了罗马的一方，而不是杀了自己.

题目：
在一个n个人组成的圆环中，我们假定从1开始报数，每当数到m时，从这个环中将这个人剔除，下一个人从1开始继续
报数，重复这一过程，直到最后一个人获胜。那么，试问：如何一开始确定一个位置，能够获得最终的胜利。
"""""
from pythonds.basic.queue import Queue


def josephus(n, m):
    """
    1.将所有人看成列表，新建一个队列存储所有人的下标，
    2.所有人开始报数，即从队列中出列，再将此人入列，直到第m个人时将此人永久出列，再继续此过程
    3.直到队列中的长度为1的时候，说明产生了最后的胜利者
    :param n: 总人数
    :param m: 报数
    :return: 序号
    """""
    person_queue = Queue()
    for i in range(n):
        person_queue.enqueue(i)
    while person_queue.size() > 1:
        for i in range(m):
            if i < m - 1:
                person_queue.enqueue(person_queue.dequeue())
            else:
                person_queue.dequeue()
    return person_queue.dequeue() + 1


if __name__ == '__main__':
    print(josephus(40, 7))

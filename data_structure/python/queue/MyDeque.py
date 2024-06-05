## 双端队列
class Deque(object):
    def __init__(self):
        self.deque = []

    ## 将item加入队首。
    def add_front(self, item):
        # 时间复杂度O(n)
        self.deque.insert(0, item)

    ## 将item加入队尾。
    def add_rear(self, item):
        # 时间复杂度O(1)
        self.deque.append(item)

    ## 从队首移除数据项, 返回值移除的数据项。
    def remove_front(self):
        # 时间复杂度O(n)
        if not self.is_empty():
            return self.deque.pop(0)

    ## 从队尾移除数据项，返回值为移除的数据项。
    def remove_rear(self):
        # 时间复杂度O(1)
        if not self.is_empty():
            return self.deque.pop()

    ## 返回deque是否为空。
    def is_empty(self):
        return self.size() == 0

    ## 返回deque中包含数据项的个数。
    def size(self):
        return len(self.deque)


if __name__ == '__main__':
    d = Deque()
    print(d.is_empty())
    print(d.add_rear(4))
    print(d.add_rear("dog"))
    print(d.add_front("cat"))
    print(d.add_front(True))
    print(d.size())
    print(d.is_empty())
    print(d.add_rear(8.4))
    print(d.remove_rear())
    print(d.remove_front())
# 自定义队列类
class Queue(object):
    def __init__(self):
        self.queue = []

    ## 将数据项item添加到队尾，无返回值。
    def enqueue(self, item):
    	# enqueue 复杂度为O(n)
        self.queue.insert(0, item)

    ## 从队首移除数据项，返回值为队首数据项，队列被修改。
    def dequeue(self):
    	# dequeue 复杂度为O(1)
        if not self.is_empty():
            return self.queue.pop()

    ## 返回是否空队列。
    def is_empty(self):
        return len(self.queue) == 0

    ## 返回对了中数据项的个数。
    def size(self):
        return len(self.queue)
    
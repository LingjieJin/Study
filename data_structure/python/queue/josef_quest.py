from MyQueue import Queue

## 约瑟夫环解法
def josef_quest(names, num):
    '''
    约瑟夫问题：
        1. 将所有的人名放入队列中；
        2. 确定报数num, 循环num次, 将队首的人出队再入队；
        3. 循环结束后, 移除队首的人；
        4. 重复循环, 直到最终队列中只剩1个人。
    '''
    if not isinstance(names, list) or len(names) == 0:
        return

    queue = Queue()

    ## 所有人入队
    for name in names:
        queue.enqueue(name)

    ## 循环num次，将队首人移出再添加到队尾。 
    ## 循环结束后，将队首的人移除
    while queue.size() > 1:
        for i in range(num):
            a = queue.dequeue()
            queue.enqueue(a)
        queue.dequeue()

    ## 返回剩余的1个人
    return queue.dequeue()


if __name__ == '__main__':

    print(josef_quest(["A", "B", "C", "D", "E", "F", "G"], 7))
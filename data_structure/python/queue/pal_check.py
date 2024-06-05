from MyDeque import Deque

## 回文数判断
def pal_check(expression):
    '''
    1. 将词加入双端队列；
    2. 从双端队列两边分别移除字符，并判断是否相等。
    3. 直到最后队列中剩下0个或1个字符。
    '''
    deque = Deque()
    ## 生成队列
    for i in expression:
        deque.add_rear(i)
    
    ## 每次判断收尾是否相同
    while deque.size() not in [0, 1]:
        if deque.remove_front() != deque.remove_rear():
            return False
    else:
        return True


if __name__ == '__main__':
    print(pal_check("abccba"))
    print(pal_check("abcba"))
    print(pal_check("abcdba"))
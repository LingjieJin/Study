# 自定义栈结构
class Stack():
    def __init__(self) -> None:
        self.stack = []
        
    ## 将item加入栈顶，无返回值。
    def push(self, item):
        self.stack.append(item)
    
    ## 将栈顶的数据项移除，并返回，栈被修改。
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        
    def peek(self):
        if not self.is_empty():
            return self.stack[self.size()-1]
        
    ## 返回是否是空栈。
    def is_empty(self):
        return len(self.stack) == 0
    
    ## 返回栈中有多少个数据项。
    def size(self):
        return len(self.stack)
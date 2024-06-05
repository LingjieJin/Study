from MyStack import Stack

## 通用括号匹配
def brackets_valid(expression):
    stack = Stack()
    
    ## 定义匹配的括号
    mapping = {
        ")": "(",
        "]": "[",
        "}": "{"
    }

    for item in expression:
        ## 如果是左括号，就压入
        if item in "([{":
            stack.push(item)
        ## 如果是右括号
        ## 需要判断
        ## 1. 如果此时栈为空，不匹配
        ## 2. 如果没法找到对应类型的括号，不匹配
        ## 否则通过，推出本次匹配的括号
        elif item in ")]}":
            if stack.is_empty():
                return False
            else:
                if stack.peek() != mapping[item]:
                    return False
                else:
                    stack.pop()

    return stack.is_empty()

## 简单的测试
if __name__ == '__main__':
    print(brackets_valid("()()()"))
    print(brackets_valid("(()())(()"))
    print(brackets_valid("((5+6)*(4+3))+((10-9)"))

    print(brackets_valid("{{([][])}()}"))
    print(brackets_valid("[[{{(())}}]]"))
    print(brackets_valid("[][][](){}"))

    print(brackets_valid("([)}"))
    print(brackets_valid("((()]))"))
    print(brackets_valid("[{()]"))
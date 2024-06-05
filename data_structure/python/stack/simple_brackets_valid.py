from MyStack import Stack

# 简单括号匹配
def simple_brackets_valid(expression):
    stack = Stack()

    for item in expression:
        if item == "(":
            stack.push(item)
        elif item == ")":
            if stack.is_empty():
                return False
            else:
                stack.pop()

    return stack.is_empty()


if __name__ == '__main__':
    print(simple_brackets_valid("()()()"))
    print(simple_brackets_valid("(()())(()"))
    print(simple_brackets_valid("((5+6)*(4+3))+((10-9)"))
    


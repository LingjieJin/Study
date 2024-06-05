from MyStack import Stack

## 简单的十进制转换二进制
def cvt_10To2(num):
    '''
    常见的十进制转换二进制采用的是除2求余数的算法。
    '''
    ## 类型检测
    if not isinstance(num, int):
        return False

    stack = Stack()
    while num:
        num, remainder = divmod(num, 2)
        stack.push(remainder)

    result = ""
    while not stack.is_empty():
        result += str(stack.pop())

    return result

## 10进制转换为2进制，8进制，16进制
def cvt_10ToX(num, unit):
    ## 类型检测
    if not isinstance(num, int):
        return False

    dights = "0123456789ABCDEF"
    stack = Stack()
    while num:
        num, remainder = divmod(num, unit)
        stack.push(remainder)

    result = ""
    while not stack.is_empty():
        result += str(dights[stack.pop()])

    return result

if __name__ == '__main__':
    ##
    print(f"35的二进制数是{cvt_10To2(35)}")
    ##
    print(f"35的二进制数是{cvt_10ToX(35, 2)}")
    print(f"233的八进制数是{cvt_10ToX(233, 8)}")
    print(f"233的十六进制数是{cvt_10ToX(233, 16)}")
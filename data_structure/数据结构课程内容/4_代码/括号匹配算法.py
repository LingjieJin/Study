# 引入系统的栈结构
from collections import deque

# 判断函数
def isValid(s):
    ## 这张表很重要，是后面匹配判断用的
    dic = {"(":")",
           "[":"]",
           "{":"}"}
    
    ## 初始化一个栈
    st = deque()
    
    ## 遍历输入的字符串
    for c in s:
        ## 如果输入的字符是前半段括号，压入栈中
        if c in "([{":
            st.append(c)
        ## 如果输入的字符是后半段括号，进入判断
        elif c in ")]}":
            ## 如果当前字符长度为0，直接返回错误
            if len(st) == 0:
                return False
            ## 推出当前应该匹配的括号与当前括号匹配
            t = st.pop()
            if dic[t] != c:
                return False
            
    return len(st) == 0

s = input()
#
# print("yes" if isValid(s) else "no")

if isValid(s):
    print("yes")
else:
    print("no")


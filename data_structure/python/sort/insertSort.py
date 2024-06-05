# 插入排序
## 默认从小到大排序
def insertSort(a):
    ## 排序数据的大小
    n = len(a)
    ## 遍历
    for i in range(1,n):
        t = a[i]    # 暂存插入数据
        ## 从后往前找到插入位置，同时从后往前移动原有的值
        j = i - 1   
        while j >= 0 and t < a[j]:
            a[j + 1] = a[j]
            j = j - 1
            
        ## 在位置J的后面插入a[i]
        a[j + 1] = t
        print("第{:^3d}次排序:".format(i), *a)
  
if __name__ == '__main__':
    a = [49, 38, 97, 76, 65, 13, 27, 50]
    insertSort(a)
    print("排序后的结果:" *a)
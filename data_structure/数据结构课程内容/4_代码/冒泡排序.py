# 冒泡排序
## 冒泡排序的时间复杂度是O(N^2),是稳定排序法，
## 因为冒泡排序的排序趟数与原始序列中数据元素的排列有关，因此，排序的趟数为一个范围，即[1 ~ n-1]。
def bubbleSort(a):
    n = len(a)
    for i in range(1, n):
        f = False  # 没有发生交换
        ## 遍历每个元素，进行比较，较大的元素往后移动
        ## 每交换一次，都有一个元素冒泡到最上方，只需要执行n-i个元素
        for j in range(n - i):
            if a[j] > a[j + 1]:  # 逆序就交换
                a[j], a[j + 1] = a[j + 1], a[j]
                f = True  # 发生交换
        if not f:  # 没有发生交换
            break
        ## 输出每次排序结果
        print(*a)


n = int(input())
a = list(map(int, input().split()))
bubbleSort(a)
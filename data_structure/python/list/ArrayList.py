## 顺序表
class ArrayList:
    ## 初始化顺序表
    ## 表的初始大小需要
    def __init__(self, size):
        self.size = size
        self.data = [None] * size
        ### 当前数据长度
        self.length = 0

    ## 判断当前表是否为空
    def is_empty(self):
        return self.length == 0

    ## 判断当前表是否塞满
    def is_full(self):
        return self.length == self.size

    ## 增加元素
    def append(self, value):
        if self.is_full():
            print("The list is full.")
            return
        self.data[self.length] = value
        self.length += 1

    ## 插入元素
    def insert(self, index, value):
        if index < 0 or index > self.length:
            print("Invalid index.")
            return
        if self.is_full():
            print("The list is full.")
            return
        for i in range(self.length, index, -1):
            self.data[i] = self.data[i - 1]
        self.data[index] = value
        self.length += 1

    ## 删除元素
    def delete(self, index):
        if index < 0 or index >= self.length:
            print("Invalid index.")
            return
        for i in range(index, self.length - 1):
            self.data[i] = self.data[i + 1]
        self.length -= 1

    ## 获取某一个元素
    def get(self, index):
        if index < 0 or index >= self.length:
            print("Invalid index.")
            return
        return self.data[index]

    ## 输出该表
    def display(self):
        print(self.data[: self.length])

if __name__ == "__main__":
    # 使用示例
    arr_list = ArrayList(5)
    arr_list.append(1)
    arr_list.append(2)
    arr_list.append(3)
    arr_list.display()

    arr_list.insert(1, 4)
    arr_list.display()

    arr_list.delete(2)
    arr_list.display()

    print(arr_list.get(1))

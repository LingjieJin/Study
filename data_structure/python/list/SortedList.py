from MyNode import Node

class SortedLinkedList(object):
    def __init__(self):
        self.head = None

    ## 添加一个数据，并保持整体有序
    def add(self, data):
        node = Node(data)
        ## 空链表
        if self.head is None:
            self.head = node
            return
        ## 比头结点小
        elif data < self.head.get_data():
            node.set_next(self.head)
            self.head = node
        ## 比头结点大
        else:
            current = self.head
            previous = self.head
            while current is not None:
                ## 如果数据比当前节点小，插入当前Node
                if data < current.get_data():
                    previous.set_next(node)
                    node.set_next(current)
                    break
                ## 循环遍历
                previous = current
                current = current.get_next()
            
            if current is None:
                ## 在最后加入这个元素
                previous.set_next(node)

    ## 删除某个数据项，并保持有序
    def remove(self, data):
        current = self.head
        previous = self.head

        while current is not None:
            if current.get_data() == data:
                previous.set_next(current.get_next())
                break
            previous = current
            current = current.get_next()

    ## 查找某个数据项
    def search(self, data):
        current = self.head

        while current is not None:
            if current.get_data() == data:
                return True
            elif current.get_data() > data:
                return False
            else:
                current = current.get_next()
        else:
            return False

    ## 判断链表是否为空
    def is_empty(self):
        return self.size() == 0

    ## 获取链表大小
    def size(self):
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.get_next()
        return count

    ## 获取某个节点的下标
    def index(self, data):
        index = 0
        current = self.head

        while current is not None:
            if current.get_data() == data:
                return index
            elif current.get_data() > data:
                return -1
            else:
                current = current.get_next()
            index += 1

        return -1

    ## 推出某个位置的节点
    def pop(self, pos=None):
        previous = self.head
        current = self.head
        index = 0
        data = None

        if self.is_empty():
            return None

        ## 如果pos值小于0，推出头结点
        if pos < 0:
            data = self.head.get_data()
            self.head.set_next(self.head.get_next())
            return data
        
        ## 遍历
        while current.get_next() is not None:
            ## 找到该节点
            if index == pos:
                ## 直接将前节点指向后节点，推出当前节点
                previous.set_next(current.get_next())
                data = current.get_data()
                break
            index += 1
            previous = current
            current = current.get_next()
        ## 找到节点
        else:
            ## 如果一直找到末尾没有匹配，则一定推出末尾元素
            if pos >= index:
                previous.set_next(current.get_next())
                data = current.get_data()

        return data
    
    
if __name__ == '__main__':
    sorted_list = SortedLinkedList() 
    sorted_list.add(5) 
    sorted_list.add(3) 
    sorted_list.add(7) 
    sorted_list.add(4) 
    sorted_list.add(6) 
    print(sorted_list.size()) 
    print(sorted_list.search(4)) 
    print(sorted_list.index(7))
    print(sorted_list.pop(4))
    print(sorted_list.pop(6))
    
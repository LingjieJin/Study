# 链表节点
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# 单链表
class SinglyLinkedList: 
    def __init__(self):
        self.head = None

    def add_node(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def delete_node(self, data):
        current = self.head
        if current.data == data:
            self.head = current.next
            return
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next

    def find_node(self, data):
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False

    def display(self):
        current = self.head
        while current:
            print(current.data, end=' ')
            current = current.next
        print()


# 使用示例
sll = SinglyLinkedList()
sll.add_node(1)
sll.add_node(2)
sll.add_node(3)
sll.delete_node(2)
sll.display()
print(sll.find_node(1))
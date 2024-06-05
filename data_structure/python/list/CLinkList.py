class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def add_node(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head

    def display(self):
        current = self.head
        if self.head:
            while True:
                print(current.data, end=' ')
                current = current.next
                if current == self.head:
                    break
        print()


# 使用示例
cll = CircularLinkedList()
cll.add_node(1)
cll.add_node(2)
cll.add_node(3)
cll.display()
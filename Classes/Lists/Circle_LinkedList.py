from Classes.Node import Node


class CircleLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            new_node.next = self.head
            return

        current_node = self.head
        while current_node.next is not self.head:
            current_node = current_node.next
        new_node.next = current_node.next
        current_node.next = new_node

    def remove(self, data):
        if self.head.data == data:
            self.head = self.head.next

        current_node = self.head
        while current_node.next is not self.head:
            if current_node.next.data == data:
                current_node.next = current_node.next.next
                return
            current_node = current_node.next

        print("Doesn't search")

    def transverse(self):
        if self.head is None:
            return
        current_node = self.head
        while True:
            print(current_node.data)
            current_node = current_node.next
            if current_node is self.head:
                break

    def exist(self, data):
        # case 1: List is empty
        if self.head is None:
            print("List is empty")
            return False

        # case 2: List is not empty or is not None
        current_node = self.head
        while current_node is not None:
            if current_node.data == data:
                return True
            current_node = current_node.next

        # case 3: We reached the end and found nothing
        return False

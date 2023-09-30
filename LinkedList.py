from Node import Node


class LinkedList:

    def __init__(self):
        self.head = None

    def add(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            return

        current_node = self.head
        while current_node.next is not None:
            if current_node.next is None:
                break
            current_node = current_node.next
        current_node.next = new_node

    def push(self, data):
        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node

    def remove(self, data):
        if self.head.data == data:
            self.head = self.head.next

        current_node = self.head
        while current_node.next is not None:
            if current_node.next.data == data:
                current_node.next = current_node.next.next
                return
            current_node = current_node.next

        return "Doesn't exist"

    def transverse(self):

        if self.head is None:
            return

        current_node = self.head
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next

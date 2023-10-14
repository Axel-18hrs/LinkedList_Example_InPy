from Node import Node


class DoublyLinkedList:

    def __init__(self):
        self.head = None

    def push(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
        current_node.next = new_node
        new_node.prev = current_node

    def add(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            return

        if new_node.data < self.head.data:
            new_node.next = self.head
            self.head = new_node
            return

        current_node = self.head
        while current_node.next is not None and current_node.next.data < new_node.data:
            current_node = current_node.next
        new_node.next = current_node.next
        new_node.prev = current_node
        current_node.next = new_node

    def remove(self, data):
        if self.head.data == data:
            self.head = self.head.next

        current_node = self.head
        while current_node.next is not None:
            if current_node.next.data == data:
                current_node.next = current_node.next.next
                current_node.next.prev = current_node
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

    def exist(self, data):
        current_node = self.head
        while current_node is not None:
            if current_node.data == data:
                return "Yes"
            current_node = current_node.next

        return "Nope"

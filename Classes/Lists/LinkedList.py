from Classes.Node import Node


class LinkedList:

    def __init__(self):
        self.head = None

    def add(self, value):
        new_node = Node(value)

        # case 1: List is empty
        if self.head is None:
            self.head = new_node
            return

        # case 2: The value already exists
        if self.exist(value):
            print("It already exists")
            return

        # case 3: The list is not empty
        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
        current_node.next = new_node

    def remove(self, data):
        # case 1: the head has the courage to remove
        if self.head.data == data:
            self.head = self.head.next
            return

        # case 2: Any of the following nodes has the value to be removed
        current_node = self.head
        while current_node.next is not None:
            if current_node.next.data == data:
                current_node.next = current_node.next.next
                return
            current_node = current_node.next

        # case 3: When we reached the end of the list and it was not found
        print("Doesn't exist")

    def transverse(self):
        # case 1: List is empty
        if self.head is None:
            print("List is empty")
            return

        # case 2: List is not empty or is not None
        current_node = self.head
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next

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

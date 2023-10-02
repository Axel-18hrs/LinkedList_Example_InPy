from Classes.Node import Node


class DoublyCircleLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, value):
        new_node = Node(value)

        # case 1: The list is empty
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return

        # # case 2: List is not empty or is not None
        # if self.exist(value):
        #     print("It already exists")
        #     return

        # case 3: The list is not empty
        current_node = self.head
        while True:
            if current_node is self.head:
                break

            current_node = current_node.next

        new_node.next = self.head
        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node

    def remove(self, data):
        # case 1: the head has the courage to remove
        if self.head.data == data:
            self.head = self.head.next
            self.tail = self.head
            return

        # case 2: Any of the following nodes has the value to be removed
        current_node = self.head
        while current_node.next is not self.head:
            if current_node.next.data == data:
                # case 2.1: When the value to be removed is the tail of the list
                if current_node.next == self.tail:
                    self.tail = current_node
                    current_node.next = self.head
                    return
                # case 2.2: When the value to be removed is not the tail of the list
                current_node.next.next.prev = current_node
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
        while True:
            print(current_node.data)
            current_node = current_node.next
            if current_node is self.head:
                break

    def transverse_reverse(self):
        # case 1: List is empty
        if self.head is None:
            print("List is empty")
            return

        # case 2: List is not empty or is not None
        current_node = self.tail
        while True:
            print(current_node.data)
            current_node = current_node.prev
            if current_node is self.tail:
                return


    def exist(self, data):
        # case 1: List is empty
        if self.head is None:
            print("List is empty")
            return False

        # case 2: List is not empty or is not None
        current_node = self.head
        while True:
            # case 2.1: We reached the end and found nothing
            if current_node.next is self.head:
                return False

            if current_node.data == data:
                return True
            current_node = current_node.next



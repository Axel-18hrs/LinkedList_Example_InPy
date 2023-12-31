from Classes.Node import Node
from Classes.Lists.Lists_Interface import ListOperations


class CircleLinkedList(ListOperations):

    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, value):
        new_node = Node(value)

        # case 1: List is empty.
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
            self.tail.next = self.head
            return

        # case 2: The value already exists
        if self.exist(value):
            print(f"- [{value}] Already exists in the list")
            return

        # case 3: Head has a value less than that of the new node
        if new_node.data < self.head.data:
            new_node.next = self.head
            self.head = new_node
            self.tail.next = self.head
            return

        # case 4: Tail has a value less than that of the new node
        if new_node.data > self.tail.data:
            self.tail.next = new_node
            self.tail = new_node
            self.tail.next = self.head
            return

        # case 5: The value will be placed in an unknown position
        current_node = self.head
        while current_node.next is not self.head and current_node.next.data < new_node.data:
            current_node = current_node.next

        new_node.next = current_node.next
        current_node.next = new_node
        pass

    def remove(self, data):
        # case 1: the head has the courage to remove
        if self.head.data == data:
            self.head = self.head.next
            self.tail.next = self.head
            print(f"- Data[{data}] was removed from the list")
            return

        # case 2: Any of the following nodes has the value to be removed
        current_node = self.head
        while current_node.next is not self.head and current_node.next.data < data:
            current_node = current_node.next

        # case 3: When the value to be removed is the tail of the list
        if current_node.next.data == data and current_node.next is self.tail:
            self.tail = current_node
            self.tail.next = self.head
            print(f"- Data[{data}] was removed from the list")
            return

        # case 4: When the value to be removed is not the tail of the list
        if current_node.next.data == data:
            current_node.next = current_node.next.next
            print(f"- Data[{data}] was removed from the list")
            return

        # case 5: When we reached the end of the list and it was not found
        print(f"- Data[{data}] Does not exist in the list")
        pass

    def show(self):
        # case 1: List is empty
        if self.is_empty():
            print("// List is empty")
            return

        # case 2: List is not empty or is not None
        print("=== My Circle list ===")
        i = 0
        current_node = self.head
        while True:
            print(f"- Node[{i}] and data: {current_node.data}")
            current_node = current_node.next
            i += 1
            if current_node is self.head:
                break
        pass

    def show_reverse(self):
        pass

    def exist(self, data):
        # case 1: List is empty
        if self.is_empty():
            print("// List is empty")
            return False

        # case 2: The 'head' node contains the value
        if self.head.data == data:
            return True

        # case 3: The 'tail' node contains the value
        if self.tail.data == data:
            return True

        # case 4: Any node in the list can have the value
        current_node = self.head
        while current_node.next is not self.head and current_node.data < data:
            current_node = current_node.next

        # case 5: The value already exists in the list
        if current_node.data == data:
            return True

        # case 6: We reached the end and found nothing
        return False
        pass

    def search(self, data):
        # case 1: List is empty
        if self.is_empty():
            print("// List is empty")
            return

        # case 2: The 'head' node contains the value
        if self.head.data == data:
            print(f"- Data[{data}] Exists in the list")
            return

        # case 3: The 'tail' node contains the value
        if self.tail.data == data:
            print(f"- Data[{data}] Exists in the list")
            return

        # case 4: Any node in the list can have the value
        current_node = self.head
        while current_node.next is not self.head and current_node.data < data:
            current_node = current_node.next

        # case 5: The value already exists in the list
        if current_node.data == data:
            print(f"- Data[{data}] Exists in the list")
            return

        # case 6: We reached the end and found nothing
        print(f"- Data[{data}] Does not exist in the list")
        return
        pass

    def is_empty(self):
        return self.head is None
        pass

    def clear(self):
        self.head = None
        self.tail = None
        pass

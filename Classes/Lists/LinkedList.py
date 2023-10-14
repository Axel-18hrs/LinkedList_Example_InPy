from Classes.Node import Node
from Classes.Lists.Lists_Interface import ListOperations


class LinkedList(ListOperations):

    def __init__(self):
        self.head = None

    def add(self, value):
        new_node = Node(value)

        # case 1: List is empty
        if self.is_empty():
            self.head = new_node
            return

        # case 2: The value already exists
        if self.exist(value):
            print("It already exists")
            return

        # case 3: Head has a value greater than that of the new node
        if self.head.data > new_node.data:
            new_node.next = self.head
            self.head = new_node
            return

        # case 3: The list is not empty
        current_node = self.head
        while current_node.next is not None and current_node.next.data < new_node.data:
            current_node = current_node.next
        new_node.next = current_node.next
        current_node.next = new_node
        pass

    def delete(self, data):
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
        pass

    def transverse(self):
        # case 1: List is empty
        if self.is_empty():
            print("List is empty")
            return

        # case 2: List is not empty or is not None
        current_node = self.head
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next
        pass

    def transverse_reverse(self):
        pass

    def exist(self, data):
        # case 1: List is empty
        if self.is_empty():
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
        pass

    # Made for israel and refactored for me
    def search(self, data):
        # case 1: List is empty
        if self.is_empty():
            print("List is empty")
            return

        # case 2: List is not empty or is not None
        current_node = self.head
        while current_node is not None:
            if current_node.data == data:
                print(f"- Dato[{data}] Existe en la lista")
                return
            current_node = current_node.next

        # case 3: The value is not in the list
        print(f"- Dato[{data}] No Existe en la lista")
        pass

    def show(self):
        # case 1: List is empty.
        if self.is_empty():
            print("List is empty")
            return

        # case 2: List is not empty or is not None
        print("=== Mi lista simple ===")
        i = 1
        current_node = self.head
        while True:
            print(f"- Nodo[{i}] y dato: {current_node.data}")
            current_node = current_node.next
            i += 1
            if current_node is None:
                break
        pass

    def is_empty(self):
        return self.head is None
        pass

    def clear(self):
        self.head = None
        pass

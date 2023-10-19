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
            print(f"- [{value}] Already exists in the list")
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
            print(f"- Data[{data}] was removed from the list")
            self.head = self.head.next
            return

        # case 2: Any of the following nodes has the value to be removed
        current_node = self.head
        while current_node.next is not None and current_node.next.data < data:
            current_node = current_node.next

        # case 3: The node to be deleted was found
        if current_node.next.data == data:
            print(f"- Data[{data}] was removed from the list")
            current_node.next = current_node.next.next
            return

        # case 4: Node not found
        print(f"- Data[{data}] Does not exist in the list")
        pass

    def transverse(self):
        # case 1: List is empty
        if self.is_empty():
            print("// List is empty")
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
            print("// List is empty")
            return False

        # case 2: The 'head' node contains the value
        if self.head.data == data:
            return True

        # case 3: Any node in the list can have the value
        current_node = self.head
        while current_node.next is not None and current_node.next.data <= data:
            current_node = current_node.next

        # case 4: The value already exists in the list
        if current_node.data == data:
            return True

        # case 5: We reached the end and found nothing
        return False
        pass

    # Made for israel and refactored for me
    def search(self, data):
        # case 1: List is empty
        if self.is_empty():
            print("// List is empty")
            return False

        # case 2: The 'head' node contains the value
        if self.head.data == data:
            print(f"- Data[{data}] was removed from the list")
            return

        # case 3: Any node in the list can have the value
        current_node = self.head
        while current_node.next is not None and current_node.next.data <= data:
            current_node = current_node.next

        # case 4: The value already exists in the list
        if current_node.data == data:
            print(f"- Data[{data}] was removed from the list")
            return

        # case 5: We reached the end and found nothing
        print(f"- Data[{data}] Does not exist in the list")
        return
        pass

    def show(self):
        # case 1: List is empty.
        if self.is_empty():
            print("// List is empty")
            return

        # case 2: List is not empty or is not None
        print("=== My simple list ===")
        i = 1
        current_node = self.head
        while True:
            print(f"- Node[{i}] and data: {current_node.data}")
            current_node = current_node.next
            i += 1
            if current_node is None:
                break
        pass

    def show_reverse(self):
        pass

    def is_empty(self):
        return self.head is None
        pass

    def clear(self):
        self.head = None
        pass

from Classes.Node import Node
from Classes.Lists.Lists_Interface import ListOperations


class LinkedList(ListOperations):

    def __init__(self):
        self.head = None

    def add(self, data):
        new_node = Node(data)

        # case 1: List is empty
        if self.is_empty():
            self.head = new_node
            return

        # case 2: The data already exists
        if self.exist(data):
            print(f"- [{data}] Already exists in the list")
            return

        # case 3: Head has a data greater than that of the new node
        if self.head.data > new_node.data:
            new_node.next = self.head
            self.head = new_node
            return

        # case 4: The value will be placed in an unknown position
        current_node = self.head
        while current_node.next is not None and current_node.next.data < new_node.data:
            current_node = current_node.next
        new_node.next = current_node.next
        current_node.next = new_node
        pass

    def remove(self, data):
        # case 1: the head has the courage to remove
        if self.head.data == data:
            print(f"- Data[{data}] was removed from the list")
            self.head = self.head.next
            return

        # case 2: Any of the following nodes has the data to be removed
        current_node = self.head
        while current_node.next is not None and current_node.next.data < data:
            current_node = current_node.next

        # case 3: The node to be removed was found
        if current_node.next.data == data:
            print(f"- Data[{data}] was removed from the list")
            current_node.next = current_node.next.next
            return

        # case 4: Node not found
        print(f"- Data[{data}] Does not exist in the list")
        pass

    def show(self):
        # case 1: List is empty.
        if self.head is None:
            print("// List is empty")
            return

        # case 2: List is not empty or is not None
        print("=== My simple list ===")
        i = 0
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

    def exist(self, data):
        # case 1: List is empty
        if self.is_empty():
            return False

        # case 2: The 'head' node contains the data
        if self.head.data == data:
            return True

        # case 3: Any node in the list can have the data
        current_node = self.head
        while current_node.next is not None and current_node.data < data:
            current_node = current_node.next

        # case 4: The data already exists in the list
        if current_node.data == data:
            return True

        # case 5: We reached the end and found nothing
        return False
        pass

    def search(self, data):
        # case 1: List is empty
        if self.is_empty():
            print("// List is empty")
            return False

        # case 2: The 'head' node contains the data
        if self.head.data == data:
            print(f"- Data[{data}] was removed from the list")
            return

        # case 3: Any node in the list can have the data
        current_node = self.head
        while current_node.next is not None and current_node.data < data:
            current_node = current_node.next

        # case 4: The data already exists in the list
        if current_node.data == data:
            print(f"- Data[{data}] was removed from the list")
            return

        # case 5: We reached the end and found nothing
        print(f"- Data[{data}] Does not exist in the list")
        return
        pass

    def is_empty(self):
        return self.head is None
        pass

    def clear(self):
        self.head = None
        pass

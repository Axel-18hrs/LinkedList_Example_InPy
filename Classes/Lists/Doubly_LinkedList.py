from Classes.DoubleNode import DoubleNode
from Classes.Lists.Lists_Interface import ListOperations


class DoublyLinkedList(ListOperations):

    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, data):
        new_node = DoubleNode(data)

        # case 1: The list is empty
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
            return

        # case 2: The value exist
        if self.exist(data):
            print(f"- [{data}] Already exists in the list")
            return

        # case 3:Head has a value greater than that of the new node
        if new_node.data < self.head.data:
            new_node.next = self.head
            self.head.back = new_node
            self.head = new_node
            return

        # case 4: The node to add goes after the Tail
        if new_node.data > self.tail.data:
            new_node.back = self.tail
            self.tail.next = new_node
            self.tail = new_node
            return

        # case 5: The value is less than a certain number of nodes
        current_node = self.head
        while current_node.next is not self.tail and current_node.next.data < new_node.data:
            current_node = current_node.next

        new_node.back = current_node
        new_node.next = current_node.next
        current_node.next.back = new_node
        current_node.next = new_node
        pass

    def remove(self, data):
        # case 1: list is empty
        if self.is_empty():
            print("// List is empty")
            return

        # case 2: the head has the courage to remove
        if self.head.data == data:
            self.head = self.head.next
            self.head.back = None
            print(f"- Data[{data}] was removed from the list")
            return

        # case 3: When the value to be removed is the tail of the list
        if self.tail.data == data:
            self.tail = self.tail.back
            self.tail.next = None
            print(f"- Data[{data}] was removed from the list")
            return

        # case 4: Any of the following nodes has the value to be removed
        current_node = self.head
        while current_node.next is not None and current_node.data < data:
            current_node = current_node.next

        # case 5: When the value to be removed is not the tail of the list
        if current_node.data == data:
            current_node.next.back = current_node.back
            current_node.back.next = current_node.next
            print(f"- Data[{data}] was removed from the list")
            return

        # case 6: When we reached the end of the list and it was not found
        print(f"- Data[{data}] Does not exist in the list")
        pass

    def show(self):
        # case 1: List is empty
        if self.is_empty():
            print("// List is empty")
            return

        # case 2: List is not empty or is not None
        print("=== My Doubly Linked List ===")
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
        # case 1: List is empty
        if self.is_empty():
            print("// List is empty")
            return

        # case 2: List is not empty or is not None
        print("=== My Reverse Doubly Linked List ===")
        i = 0
        current_node = self.tail
        while True:
            print(f"- Node[{i}] and data: {current_node.data}")
            current_node = current_node.back
            i += 1
            if current_node is None:
                break
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
        while current_node.next is not None and current_node.next.data <= data:
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
        while current_node.next is not None and current_node.next.data <= data:
            current_node = current_node.next

        # case 5: The value already exists in the list
        if current_node.data == data:
            print(f"- Data[{data}] Exists in the list")
            return

        # case 6: We reached the end and found nothing
        print(f"- Data[{data}] Does not exists in the list")
        return
        pass

    def is_empty(self):
        return self.head is None
        pass

    def clear(self):
        self.head = None
        self.tail = None
        pass

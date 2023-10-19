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
            new_node.next = self.head
            return

        # case 2: The value already exists
        if self.exist(value):
            print(f"- [{value}] Ya existe en la lista")
            return

        # case 3: Head has a value less than that of the new node
        if self.head.data > new_node.data:
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

        # case 5: The value is less than one of the nodes in the list.
        current_node = self.head
        while current_node.next is not self.head and current_node.next.data < new_node.data:
            current_node = current_node.next

        new_node.next = current_node.next
        current_node.next = new_node
        pass

    def delete(self, data):
        # case 1: the head has the courage to remove
        if self.head.data == data:
            print(f"- Dato[{data}] Se elimino de la lista")
            self.head = self.head.next
            self.tail.next = self.head
            return

        # case 2: Any of the following nodes has the value to be removed
        current_node = self.head
        while current_node.next is not self.head and current_node.next.data < data:
            current_node = current_node.next

        # case 3: When the value to be removed is the tail of the list
        if current_node.next.data == data and current_node.next is self.tail:
            print(f"- Dato[{data}] Se elimino de la lista")
            self.tail = current_node
            self.tail.next = self.head
            return

        # case 4: When the value to be removed is not the tail of the list
        if current_node.next.data == data:
            print(f"- Dato[{data}] Se elimino de la lista")
            current_node.next = current_node.next.next
            return

        # case 5: When we reached the end of the list and it was not found
        print(f"- Dato[{data}] No Existe en la lista")
        pass

    def transverse(self):
        # case 1: List is empty
        if self.is_empty():
            print("List is empty")
            return

        # case 2: List is not empty or is not None
        current_node = self.head
        while True:
            print(current_node.data)
            current_node = current_node.next
            if current_node is self.head:
                break
        pass

    def transverse_reverse(self):
        pass

    def exist(self, data):
        # case 1: List is empty
        if self.is_empty():
            print("// La lista esta vacia")
            return False

        # case 2: The 'head' node contains the value
        if self.head.data == data:
            return True

        # case 3: The 'tail' node contains the value
        if self.tail.data == data:
            return True

        # case 4: Any node in the list can have the value
        current_node = self.head
        while current_node.next is not self.head and current_node.next.data <= data:
            current_node = current_node.next

        # case 5: The value already exists in the list
        if current_node.data == data:
            return True

        # case 6: We reached the end and found nothing
        return False
        pass

    # Made for israel and refactored for me
    def search(self, data):
        # case 1: List is empty
        if self.is_empty():
            print("// La lista esta vacia")
            return

        # case 2: The 'head' node contains the value
        if self.head.data == data:
            print(f"- Dato[{data}] Existe en la lista")
            return

        # case 3: The 'tail' node contains the value
        if self.tail.data == data:
            print(f"- Dato[{data}] Existe en la lista")
            return

        # case 4: Any node in the list can have the value
        current_node = self.head
        while current_node.next is not self.head and current_node.next.data <= data:
            current_node = current_node.next

        # case 5: The value already exists in the list
        if current_node.data == data:
            print(f"- Dato[{data}] Existe en la lista")
            return

        # case 6: We reached the end and found nothing
        print(f"- Dato[{data}] No Existe en la lista")
        return
        pass

    def show_reverse(self):
        pass

    def show(self):
        # case 1: List is empty
        if self.is_empty():
            print("// La lista esta vacia")
            return

        # case 2: List is not empty or is not None
        print("=== Mi lista simple ===")
        i = 1
        current_node = self.head
        while True:
            print(f"- Nodo[{i}] y dato: {current_node.data}")
            current_node = current_node.next
            i += 1
            if current_node is self.head:
                break
        pass

    def is_empty(self):
        return self.head is None
        pass

    def clear(self):
        self.head = None
        self.tail = None
        pass

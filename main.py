import sys
from Classes.Lists.LinkedList import LinkedList
from Classes.Lists.Doubly_LinkedList import DoublyLinkedList
from Classes.Lists.Circle_LinkedList import CircleLinkedList
from Classes.Lists.DoublyCircle_LinkedList import DoublyCircleLinkedList


def operation(value):
    match value:
        case 1:
            s_list = LinkedList()
            s_list.add(5)
            s_list.add(3)
            s_list.add(1)
            s_list.add(2)
            s_list.add(4)
            s_list.show()
            s_list.search(100)
            s_list.remove(1)
            s_list.show()
            s_list.search(1)
            print()

        case 2:
            c_list = CircleLinkedList()
            c_list.add(5)
            c_list.add(3)
            c_list.add(1)
            c_list.add(2)
            c_list.add(4)
            c_list.show()
            c_list.search(100)
            c_list.remove(5)
            c_list.show()
            c_list.search(1)
            c_list.search(3)
            c_list.search(2)
            c_list.search(433)
            print()

        case 3:
            doubly_list = DoublyLinkedList()
            doubly_list.add(5)
            doubly_list.add(3)
            doubly_list.add(1)
            doubly_list.add(2)
            doubly_list.add(4)
            doubly_list.show()
            doubly_list.show_reverse()
            doubly_list.search(100)
            doubly_list.search(4)
            doubly_list.remove(1)
            doubly_list.remove(4)
            doubly_list.remove(4)
            doubly_list.show()
            doubly_list.show_reverse()
            doubly_list.search(1)
            print()

        case 4:
            cd_list = DoublyCircleLinkedList()
            cd_list.add(5)
            cd_list.add(3)
            cd_list.add(1)
            cd_list.add(2)
            cd_list.add(4)
            cd_list.show()
            cd_list.show_reverse()
            cd_list.search(100)
            cd_list.search(3)
            cd_list.show()
            cd_list.show_reverse()
            cd_list.search(1)
            print()

        case 5:
            input("End of program...")
            sys.exit()

        case x:
            input("Enter a value from (1 to 5)...")


while True:
    print("# See all Lists #\n" +
           "[1] Simple list. \n" +
           "[2] Circular list.\n" +
           "[3] Double linked list.\n" +
           "[4] Circular double linked list.\n" +
           "[5] Exit.")

    try:
        operation(int(input("Enter an option (1 - 5): ")))

    except ValueError:
        print()
        input("Enter an option (1 - 5)...")
        print("\n" * 10)

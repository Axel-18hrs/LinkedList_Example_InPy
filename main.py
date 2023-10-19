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
            s_list.delete(1)
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
            c_list.delete(1)
            c_list.show()
            c_list.search(1)
            print()

        case 3:
            doubly_list = DoublyLinkedList()
            doubly_list.add(5)
            doubly_list.add(3)
            doubly_list.add(1)
            doubly_list.add(2)
            doubly_list.add(4)
            doubly_list.show()
            doubly_list.search(100)
            doubly_list.delete(1)
            doubly_list.show()
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
            cd_list.search(100)
            cd_list.delete(1)
            cd_list.show()
            cd_list.search(1)
            print()

        case 5:
            input("Fin del programa...")
            sys.exit()

        case x:
            input("Ingresa un valor de (1 a 5)...")


while True:
    print("# Ver todas las Listas #\n" +
          "[1] Lista simple.\n" +
          "[2] Lista circular.\n" +
          "[3] Lista doble enlazada.\n" +
          "[4] Lista circular doble enlazada.\n" +
          "[5] Salir.")

    try:
        operation(int(input("Ingresa una opción (1 - 5): ")))

    except ValueError:
        print()
        input("Ingresa un valor de (1 a 5)...")
        print("\n" * 10)

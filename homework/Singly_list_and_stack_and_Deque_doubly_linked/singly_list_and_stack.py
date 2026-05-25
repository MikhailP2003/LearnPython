class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class SinglyLinkedList:

    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node

    def prepend(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def remove(self, value):
        if self.head is None:
            print("Список пуст")
            return
        if self.head.value == value:
            self.head = self.head.next
            return
        current = self.head
        while current.next is not None:
            if current.next.value == value:
                current.next = current.next.next
                return
            current = current.next
        print("Элемент не найден")

    def print_list(self):
        if self.head is None:
            print("Список пуст")
            return
        current = self.head
        while current is not None:
            print(current.value, end=" -> ")
            current = current.next

        print("None")


class Stack:

    def __init__(self):
        self.top = None

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.top is None:
            print("Стек пуст")
            return None

        value = self.top.value
        self.top = self.top.next
        return value

    def peek(self):
        if self.top is None:
            print("Стек пуст")
            return None
        return self.top.value

    def is_empty(self):
        return self.top is None

    def print_stack(self):
        if self.top is None:
            print("Стек пуст")
            return
        current = self.top
        print("Вершина стека")
        while current is not None:
            print(current.value)
            current = current.next
        print("Дно стека")


def main():
    print("ОДНОСВЯЗНЫЙ СПИСОК")
    linked_list = SinglyLinkedList()

    linked_list.append(10)
    linked_list.append(20)
    linked_list.append(30)
    linked_list.prepend(5)

    print("Список после добавления элементов:")
    linked_list.print_list()

    linked_list.remove(20)

    print("Список после удаления числа 20:")
    linked_list.print_list()

    print()
    print("СТЕК НА ОДНОСВЯЗНОМ СПИСКЕ")
    stack = Stack()

    stack.push(1)
    stack.push(2)
    stack.push(3)

    print("Стек после добавления элементов:")
    stack.print_stack()

    print("Удалили из стека:", stack.pop())
    print("Верхний элемент теперь:", stack.peek())

    print("Стек после удаления:")
    stack.print_stack()


main()

class DoubleNode:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


class Deque:
    def __init__(self):
        self.front = None
        self.back = None

    def push_front(self, value):
        new_node = DoubleNode(value)
        if self.front is None:
            self.front = new_node
            self.back = new_node
            return
        new_node.next = self.front
        self.front.prev = new_node
        self.front = new_node

    def push_back(self, value):
        new_node = DoubleNode(value)
        if self.back is None:
            self.front = new_node
            self.back = new_node
            return
        new_node.prev = self.back
        self.back.next = new_node
        self.back = new_node

    def pop_front(self):
        if self.front is None:
            print("Дек пуст")
            return None
        value = self.front.value
        if self.front == self.back:
            self.front = None
            self.back = None
            return value
        self.front = self.front.next
        self.front.prev = None
        return value

    def pop_back(self):
        if self.back is None:
            print("Дек пуст")
            return None
        value = self.back.value
        if self.front == self.back:
            self.front = None
            self.back = None
            return value
        self.back = self.back.prev
        self.back.next = None
        return value

    def peek_front(self):
        if self.front is None:
            print("Дек пуст")
            return None
        return self.front.value

    def peek_back(self):
        if self.back is None:
            print("Дек пуст")
            return None
        return self.back.value

    def is_empty(self):
        return self.front is None

    def print_deque(self):
        if self.front is None:
            print("Дек пуст")
            return
        current = self.front
        while current is not None:
            print(current.value, end=" <-> ")
            current = current.next
        print("None")


def main():
    print("ДЕК НА ДВУСВЯЗНОМ СПИСКЕ")

    deque = Deque()

    deque.push_back(10)
    deque.push_back(20)
    deque.push_front(5)
    deque.push_back(30)

    print("Дек после добавления элементов:")
    deque.print_deque()

    print("Первый элемент:", deque.peek_front())
    print("Последний элемент:", deque.peek_back())

    print("Удалили из начала:", deque.pop_front())
    print("Удалили из конца:", deque.pop_back())

    print("Дек после удаления:")
    deque.print_deque()


main()

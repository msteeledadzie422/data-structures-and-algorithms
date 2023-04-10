class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def __str__(self): # Same as to_string
        current = self.head
        string = ''
        while current is not None:
            string += f'{{ {current.value} }} -> '
            current = current.next
        return string + 'NULL'

    # LL: (3) -> (8) -> (2) -> None
    #                           ^
    # Head : 2
    # Current : 1
    def traverse_list(self):
        current = self.head
        while current is not None:
            current.value += 1
            current = current.next
        return "something"

    def insert(self, value):
        self.head = Node(value, self.head)

    def includes(self, value):
        current = self.head
        while current is not None:
            if current.value == value:
                return True
            else:
                current = current.next
        return False

    def append(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
            return
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = node

    def insert_before(self, value, new_value):
        if self.head is None:
            raise TargetError("The linked list is empty.")
        if self.head.value == value:
            self.head = Node(new_value, self.head)
            return
        current = self.head
        while current.next is not None and current.next.value != value:
            current = current.next
        if current.next is None:
            raise TargetError(f"Target value {value} not found in the linked list.")
        current.next = Node(new_value, current.next)

    def insert_after(self, value, new_value):
        current = self.head
        while current is not None and current.value != value:
            current = current.next
        if current is not None:
            current.next = Node(new_value, current.next)
        else:
            raise TargetError

    def kth_from_end(self, k):
        if k < 0:
            raise TargetError("k must be a non-negative integer")

        current = self.head
        length = 0
        while current:
            current = current.next
            length += 1

        if k >= length:
            raise TargetError(f"k value {k} is out of range")

        current = self.head
        for _ in range(length - k - 1):
            current = current.next
        return current.value


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class TargetError(Exception):
    pass

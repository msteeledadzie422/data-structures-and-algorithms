class LinkedList:
    """
    A singly-linked list.
    Attributes:
        head (Node): The first node in the linked list.
    """

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
        if self.head is not None and self.head.value == value:
            self.head = Node(new_value, self.head)
            return
        current = self.head
        while current.next is not None and current.next.value != value:
            current = current.next
        current.next = Node(new_value, current.next)

    def insert_after(self, value, new_value):
        current = self.head
        while current is not None and current.value != value:
            current = current.next
        if current is not None:
            current.next = Node(new_value, current.next)

    # def __str__(self):
    #     current = self.head
    #     string = ""
    #     while current is not None:
    #         string += f'{{{current.value}}} -> '
    #         current = current.next
    #     string += 'NULL'
    #     return string

class Node:
    def __init__(self, value, next=None):
        # value, next
        self.value = value
        self.next = next
    # Node(3, node2)
    # Node.value = 3
    # Node._next = node2

class TargetError:
    """
    Doc String GOes Here
    """
    pass



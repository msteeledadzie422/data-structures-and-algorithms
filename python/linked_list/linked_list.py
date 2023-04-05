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

    # def __str__(self):
    #     current = self.head
    #     string = ""
    #     while current is not None:
    #         string += f'{{{current.value}}} -> '
    #         current = current.next
    #     string += 'NULL'
    #     return string

class Node:
    """
    A node in a singly-linked list.
    Attributes:
        value (any): The value stored in the node.
        next (Node): The next node in the list.
    """
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


if __name__ == "__main__" :
    ll = LinkedList()
    ll.insert("apple")
    print(ll)

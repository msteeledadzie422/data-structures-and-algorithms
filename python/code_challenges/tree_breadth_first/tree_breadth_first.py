class InvalidOperationError(Exception):
    pass


class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, value):
        self.items.append(value)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.items.pop(0)

    def is_empty(self):
        return len(self.items) == 0


class BinaryTree:
    def __init__(self, root=None):
        self.root = root

    def pre_order(self, values=[]):
        def traverse(input_node, value_list):
            if not input_node:
                return
            value_list.append(input_node.value)
            traverse(input_node.left, value_list)
            traverse(input_node.right, value_list)

        traverse(self.root, values)
        return values

    def in_order(self, values=[]):
        def traverse(input_node, value_list):
            if not input_node:
                return
            traverse(input_node.left, value_list)
            value_list.append(input_node.value)
            traverse(input_node.right, value_list)

        traverse(self.root, values)
        return values

    def post_order(self, values=[]):
        def traverse(input_node, value_list):
            if not input_node:
                return
            traverse(input_node.left, value_list)
            traverse(input_node.right, value_list)
            value_list.append(input_node.value)

        traverse(self.root, values)
        return values


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def breadth_first(tree):
    result = []
    if not tree.root:
        return result

    queue = Queue()
    queue.enqueue(tree.root)

    while not queue.is_empty():
        node = queue.dequeue()
        result.append(node.value)

        if node.left:
            queue.enqueue(node.left)
        if node.right:
            queue.enqueue(node.right)

    return result


if __name__ == '__main__':
    bt = BinaryTree()
    node3 = Node(3)
    node1 = Node(1)
    node7 = Node(7, node3, node1)
    node5 = Node(5)
    node11 = Node(11)
    node18 = Node(18, node5, node11)
    node4 = Node(4, node7, node18)
    bt.root = node4
    print(breadth_first(bt))


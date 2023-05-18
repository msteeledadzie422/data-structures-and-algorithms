class KaryTree:
    def __init__(self, root=None):
        self.root = root

    def pre_order(self, node=None):
        if node is None:
            node = self.root

        values = [node.value]
        for child in node.children:
            values.extend(self.pre_order(child))

        return values


class Node:
    def __init__(self, value, children=None):
        self.value = value
        self.children = children or []


def fizz_buzz_tree(root):
    def fizz_buzz(node):
        if node.value % 3 == 0 and node.value % 5 == 0:
            value = "FizzBuzz"
        elif node.value % 3 == 0:
            value = "Fizz"
        elif node.value % 5 == 0:
            value = "Buzz"
        else:
            value = str(node.value)

        new_node = Node(value, [fizz_buzz(child) for child in node.children])
        return new_node

    fizz_buzz_root = fizz_buzz(root)
    return fizz_buzz_root


if __name__ == '__main__':
    k_tree = KaryTree()
    node3 = Node(3)
    node1 = Node(1)
    node7 = Node(7, [node3, node1])
    node5 = Node(5)
    node11 = Node(11)
    node18 = Node(18, [node5, node11])
    node4 = Node(4, [node7, node18])
    k_tree.root = node4

    fizz_buzz_root = fizz_buzz_tree(k_tree.root)
    print(k_tree.pre_order(fizz_buzz_root))


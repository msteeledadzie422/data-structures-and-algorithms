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

    def find_maximum_value(self):
        if self.root is None:
            return None

        max_value = self.root.value
        stack = [self.root]
        while stack:
            current = stack.pop()
            if current.value > max_value:
                max_value = current.value
            if current.left is not None:
                stack.append(current.left)
            if current.right is not None:
                stack.append(current.right)

        return max_value


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


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
    print(bt.pre_order())
    print(bt.in_order())
    print(bt.post_order())

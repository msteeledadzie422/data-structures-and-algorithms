class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def push(self, value):
        top = self.top
        result = Node(value)
        result.next = top
        self.top = result

    def pop(self):
        temp = self.top
        if self.isEmpty():
            return 'Empty'
        self.top = temp.next
        return temp.value

    def peek(self):
        top = self.top
        if self.isEmpty():
            return 'Empty'
        return top.value

    def isEmpty(self):
        top = self.top
        if not top:
            return True
        else:
            return False


def multi_bracket_validation(str):
    stack = Stack()

    for i in range(len(str)):
        x = str[i]

        if x == '(' or x == '{' or x == '[':
            stack.push(x)
        elif (stack.top == '(' and x == ')') or (stack.top == '{' and x == '}') or (stack.top == '[' and x == ']'):
            stack.pop()
        else:
            return False
    return False if stack.top else True


multi_bracket_validation('()[]{}')


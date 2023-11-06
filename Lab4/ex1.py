class Stack:
    def __init__(self, *args):
        if len(args):
            self.items = list(args)
        else:
            self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            return None

        return self.items.pop()

    def peek(self):
        if self.is_empty():
            return None

        return self.items[-1]

    def size(self):
        return len(self.items)


if __name__ == '__main__':
    stack = Stack(1, 2)
    stack.push(3)
    stack.push(0)
    print(stack.peek())
    print(stack.size())

    print("Stack items:")
    while not stack.is_empty():
        print(stack.pop())

    print(stack.pop())

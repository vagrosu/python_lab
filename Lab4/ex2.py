class Queue:
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

        return self.items.pop(0)

    def peek(self):
        if self.is_empty():
            return None

        return self.items[0]

    def size(self):
        return len(self.items)


if __name__ == '__main__':
    queue = Queue('1', 2)
    queue.push('3')
    queue.push(0)
    print(queue.peek())
    print(queue.size())

    print("Queue items:")
    while not queue.is_empty():
        print(queue.pop())

    print(queue.pop())

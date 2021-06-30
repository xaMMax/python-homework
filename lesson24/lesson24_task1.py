# standart Stack
# class Stack:
#     def __init__(self):
#         self.items = []
#
#     def isEmpty(self):
#         return self.items == []
#
#     def push(self, item):
#         self.items.append(item)
#
#     def pop(self):
#         return self.items.pop()
#
#     def peek(self):
#         return self.items[len(self.items) - 1]
#
#     def size(self):
#         return len(self.items)
#
# s = Stack()
# s.push(1)
# s.push(5)
# s.push(3)
# s.push(7)
# print(s.size(), s.peek(), s.isEmpty(), s.items, s.pop())

# reverse Stack
class Stack1:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.insert(0, item)

    def pop(self):
        return self.items.pop(0)

    def peek(self):
        return self.items[0]

    def size(self):
        return len(self.items)

# n = Stack1()
# n.push(1)
# n.push(5)
# n.push(3)
# n.push(7)
# print(n.size(), n.peek(), n.isEmpty(), n.items, n.pop())


def read(symbols):
    n = Stack1()
    for symbol in symbols:
        n.push(symbol)
    print(n.items)


new_list = [1, 2, 3, 5, 6, 7, 8, 4, 3]
read(new_list)

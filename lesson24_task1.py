# standart Stack
class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


s = Stack()
new_list = [1, 2, 3, 5, 6, 7, 8, 4, 3]

for item in new_list:
    s.push(item)
print(s.items)

for i in range(s.size()):
    print(s.pop())


# reverse Stack
# class Stack1:
#     def __init__(self):
#         self.items = []
#
#     def isEmpty(self):
#         return self.items == []
#
#     def push(self, item):
#         self.items.insert(0, item)
#
#     def pop(self):
#         return self.items.pop(0)
#
#     def peek(self):
#         return self.items[0]
#
#     def size(self):
#         return len(self.items)



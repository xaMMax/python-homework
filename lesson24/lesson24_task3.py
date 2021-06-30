# standart Stack with 'get_from_stack' function
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
#     def get_from_stack(self, item):
#         if item in self.items:
#             self.items.remove(item)
#             return item
#         else:
#             raise ValueError(f"I haven't element {item}")
#
#
# s = Stack()
# s.push(1)
# s.push(5)
# s.push(3)
# s.push(7)
# s.push('e')
# s.push('i')
# print(s.items)
# print(s.get_from_stack('e'), s.items)
# print(s.get_from_stack(6), s.items)

# Standart Quene with 'get_from_stack' function
class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def get_from_stack(self, item):
        if item in self.items:
            self.items.remove(item)
            return item
        else:
            raise ValueError(f"I haven't element {item}")

q = Queue()
q.enqueue(1)
q.enqueue(5)
q.enqueue(3)
q.enqueue(7)
q.enqueue('e')
q.enqueue('i')
print(q.items)


print(q.get_from_stack('e'), q.items)
# print(q.get_from_stack(6), q.items)



class WithIndex:
    def __init__(self, iterable, start = 0):
        self.iterable = iterable
        self.start = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.start < len(self.iterable):
            i = self.iterable[self.start]
            self.start += 1
            return self.start-1, i
        else:
            raise StopIteration


spisok = ['a', 'b', 'c', 'd', 'e', 'f']
withindex = WithIndex
for i in withindex(spisok):
    print(i)

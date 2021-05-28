class Iterator:
    def __init__(self, start, end, step=1):
        self.start = start
        self.end = end
        self.step = step

    def __iter__(self):
        return self
    def __next__(self):
        if self.start > self.end:
            raise StopIteration
        self.start += self.step
        return self.start


in_range = Iterator
in_range = in_range(0,20,5)

for x in in_range:
    print(x)

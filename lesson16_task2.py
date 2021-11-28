class Iterator:
    def __init__(self, start=0, end=None, step=1):
        if end == None:
            end = start
            self.start = 0
            self.end = end
            self.step = step
        else:
            self.start = start
            self.end = end
            self.step = step

    def __iter__(self):
        return self
    def __next__(self):
        return_value = self.start
        if self.start < self.end:
            self.start += self.step
        else:
            raise StopIteration
        return return_value


in_range = Iterator
for x in in_range(2, 20, 2):
    print(x)

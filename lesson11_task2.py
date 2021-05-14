class Mathematician:

    def __init__(self, num):
        self.num = num

    def square_nums(self):
        return list(map(lambda x: pow(x, 2), self.num))

    def remove_positives(self):
        return [i for i in self.num if i <= 0]

    def filter_leaps(self):
        return [i for i in self.num if i % 4 == 0]


m = Mathematician([7, 11, 5, 4])
print(m.square_nums())
mn = Mathematician([26, -11, -8, 13, -90])
print(mn.remove_positives())
nmn = Mathematician([2001, 1884, 1995, 2003, 2020])
print(nmn.filter_leaps())

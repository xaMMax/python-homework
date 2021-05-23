class Mathematician:

    def __init__(self):
        pass
    @classmethod
    def square_nums(cls, *args):
        print(list(map(lambda x: pow(x, 2), args)))
    @classmethod
    def remove_positives(cls, *args):
        print([i for i in args if i <= 0])
    @classmethod
    def filter_leaps(cls, *args):
        print([i for i in args if i % 4 == 0])

m = Mathematician

m.square_nums(7, 11, 5, 4)
m.remove_positives(26, -11, -8, 13, -90)
m.filter_leaps(2001, 1884, 1995, 2003, 2020)


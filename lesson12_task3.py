from fractions import Fraction


class Fractions_class:
    def __init__(self, x):
        x = x.split('/')
        self.x = Fraction(int(x[0]))/Fraction(int(x[1]))

    def __add__(self, other):
        return self.x + other.x

    def __truediv__(self, other):
        return other.x / self.x

    def __sub__(self, other):
        return self.x - other.x

    def __mul__(self, other):
        return self.x * other.x


x = Fractions_class('1/4')
y = Fractions_class('3/4')
print(x + y)
print(x - y)
print(x * y)
print(x / y)

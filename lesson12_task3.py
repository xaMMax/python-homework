# from fractions import Fraction
#
#
# class Fractions_class:
#     def __init__(self, x):
#         x = x.split('/')
#         self.x = Fraction(int(x[0]))/Fraction(int(x[1]))
#
#     def __add__(self, other):
#         return self.x + other.x
#
#     def __truediv__(self, other):
#         return other.x / self.x
#
#     def __sub__(self, other):
#         return self.x - other.x
#
#     def __mul__(self, other):
#         return self.x * other.x
#
#
# x = Fractions_class('1/2')
# y = Fractions_class('1/3')
# print(x + y)
# print(x - y)
# print(x * y)
# print(x / y)
#
#ТАМ ВВЕРХУ НЕПРАВИЛЬНО СЧИТАЕТ ДЕЛЕНИЕ ОКАЗЫВАЕТСЯ...

import math


class Fractions:
    def __init__(self, x, y):
        x = x.split('/')
        y = y.split('/')
        self.numerator_x = int(x[0])
        if int(x[1]) != 0:
            self.denominator_x = int(x[1])
        else:
            raise ZeroDivisionError('You can`t divide by zero')
        self.numerator_y = int(y[0])
        if int(y[1]) != 0:
            self.denominator_y = int(y[1])
        else:
            raise ZeroDivisionError('You can`t divide by zero')

    def __add__(self):
        x = (self.numerator_x * self.denominator_y + self.numerator_y * self.denominator_x)
        y = (self.denominator_x * self.denominator_y)
        frac = math.gcd(x, y)
        print(f'summ of fractions = {x // frac}/{y // frac}')

    def __sub__(self):
        x = (self.numerator_x * self.denominator_y - self.numerator_y * self.denominator_x)
        y = (self.denominator_x * self.denominator_y)
        frac = math.gcd(x, y)
        print(f'substract of fractions = {x // frac}/{y // frac}')

    def __mul__(self):
        x = self.numerator_x * self.numerator_y
        y = self.denominator_x * self.denominator_y
        frac = math.gcd(x, y)
        print(f'multiply of fractions = {x//frac}/{y//frac}')

    def __truediv__(self):
        x = self.numerator_x * self.denominator_y
        y = self.denominator_x * self.numerator_y
        frac = math.gcd(x, y)
        print(f'division of fractions = {x // frac}/{y // frac}')



fraction = Fractions('1/0', '1/2')
fraction.__add__()
fraction.__sub__()
fraction.__mul__()
fraction.__truediv__()


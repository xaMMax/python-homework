from operator import  sub
from functools import reduce


def make_operation(x='', *args):  # define the function called make_operation
    result = 1  # use variable for use in operatoins
    # multiplication
    if x == '*':  # if else statement for choice the type of operation
        for i in args:
            result *= i
        print(result)
    # addition
    elif x == '+':
        result = sum(args)
        print(result)
    # subtraction
    elif x == '-':
        result = reduce(sub, args)
        print(result)
    # if x not equal '*', '+', '-'
    else:
        print('it is bad idea')
    return   # return result of operations


make_operation('-', 5, 6, 2, -8)  # call the function


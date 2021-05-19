# import logging
# from functools import lru_cache
import time
import math



now = time.time()
def print_argument(func):
    def wrapper(the_number):
        print("Argument for", func.__name__, "is", the_number)
        return func(the_number)
    return wrapper

def factor(x):
    return math.factorial(50000)
print(factor(1))
print(time.time() - now)

now = time.time()
@print_argument
def factor(x):
    return math.factorial(50000)
print(factor(1))
print(time.time() - now)












# @lru_cache
# def count_vowels(sentence):
#     sentence = sentence.casefold()
#     return sum(sentence.count(vowel) for vowel in 'aeiou')
#
# now = time.time() заморозка времени
# print(count_vowels('Heeello world'))
# print(time.time() - now)
# print(count_vowels.cache_info())
#
# print(time.time() - now)
# print(count_vowels('Heeello world'))
# print(time.time() - now)
# print(count_vowels.cache_info())
#
# from functools import  wraps
#
# def decorator_name(f):
#     def decorated(*args, **kwargs)
#         return f(*args, **kwargs)
#     return decorated



# from contextlib import contextmanager
# import sqlite3
#
# @contextmanager
# def db_open(db_name):
#     con = sqlite3.connect(db_name)
#     try:
#         yield con
#     finally:
#         con.close()
#
# with db_open('test.db') as con:
#     cur = con.cursor()
#     data = cur.execute("SELECT * FROM stocks")
#     for record in data:
#         print(record)
# from typing import Iterable

#
# def remove_all_before(items: list, border: int):
#     items = items[border-1:]
#     # your code here
#     return items
#
# print(remove_all_before([1, 2, 3, 4, 5], 3))
# print(remove_all_before([1, 1, 2, 2, 3, 3], 2))# [2, 2, 3, 3]
# print(remove_all_before([1, 1, 2, 4, 2, 3, 4], 2)) #[2, 4, 2, 3, 4]
# print(remove_all_before([1, 1, 5, 6, 7], 2))# [1, 1, 5, 6, 7]
# print(remove_all_before([], 0)) #[]
# print(remove_all_before([7, 7, 7, 7, 7, 7, 7, 7, 7], 7))

# def is_all_upper(text: str) -> bool:
#     for text in text.strip():
#         if text.isupper():
#             return True
#         else:
#             return False
#
# print(is_all_upper('ALL UPPER'))
# print(is_all_upper('all lower'))
# print(is_all_upper('mixed UPPER and lower'))
# print(is_all_upper(''))
# print(is_all_upper('     '))
# print(is_all_upper('444'))
# print(is_all_upper('55 55 5'))


# x = 56
# x = map(int, str(x))
# print(max(x))
#
# from textwrap import wrap
#
# def split_pairs(a):
#     # your code here
#     if len(a) % 2 == 0:
#         a = wrap(a,2)
#     else:
#         a = a + '_'
#         a = wrap(a,2)
#     return a
# print(split_pairs('abc'))
#
# def beginning_zeros(number: str):
#     a = 0
#     for x in number:
#         if x != '0':
#             break
#         else:
#             a += 1
#     print(a)
#
#
#
#
#
# (beginning_zeros('001'))
# (beginning_zeros('101'))
# # (beginning_zeros('012345679'))

#
# def correct_sentence(text: str) -> str:
#     """
#         returns a corrected sentence which starts with a capital letter
#         and ends with a dot.
#     """
#     # your code here
#     if text[-1] != '.':
#         text = ((text[0].title()) +(text[1:])+ text[-1].join('.'))
#     else:
#         text = ((text[0].title()) + (text[1:]))
#     return text
#
#
# print(correct_sentence("greetings, friends"))
# print(correct_sentence("greetings, friends"))
# print(correct_sentence("Greetings, friends"))
# print(correct_sentence("Greetings, friends."))
# print(correct_sentence("hi"))
# print(correct_sentence("welcome to New York"))
#
# def sum_numbers(text: str) -> int:
#     text = text.split()
#     s = sum([int(num) for num in filter(lambda num: num.isnumeric(), text)])
#     return s
#
#
#
#     # These "asserts" are used for self-checking and not for an auto-testing
# print(sum_numbers('hi'))
# print(sum_numbers('who is 1st here'))
# print(sum_numbers('my numbers is 2'))
# print(sum_numbers('This picture is an oil on canvas '
#                     'painting by Danish artist Anna '
#                     'Petersen between 1845 and 1910 year'))
# print(sum_numbers('5 plus 6 is'))
# # print(sum_numbers(''))
# def f(value):
#    while True:
#       value = (yield value)
#
# a = f(10)
# print(next(a))
# print(a.send(20))
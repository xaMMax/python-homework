def with_index(iterable, start=0):
    for x in iterable:
        start = start + 1
        print(x, start)


spisok = ['a', 'b', 'c', 'd', 'e', 'f']

with_index(spisok, 0)

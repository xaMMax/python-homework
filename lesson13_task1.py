def some_function_with_variables():
    a = 10
    b = 'anme'
    c = str(a ** 2)
    d = (a, b)


def locals_count(x):
    return x.__code__.co_nlocals


print(locals_count(some_function_with_variables))


def logger(func):
    def arguments(*args):
        print(f'{func.__name__} called with {args}')
        return func(*args)
    return arguments

@logger
def add(x, y):
    return x+y

@logger
def square_all(*args):
    return [arg**2 for arg in args]


print(add(4,5))

print(square_all(2,5,8,9))

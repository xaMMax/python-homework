def logger(func):
    def args(*args):
        print(f'{func.__name__} called with {args}')
    return args

@logger
def add(x, y):
    return x+y

@logger
def square_all(*args):
    return [arg**2 for arg in args]


add(4,5)

square_all(2,5,8,9)
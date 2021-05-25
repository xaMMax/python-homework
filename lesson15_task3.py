class TypeDecorators:
    def __init__(self, *args):
        self.args = args
    @staticmethod
    def to_int(func):
        def converter(*args, **kwargs):
            x = (args[0])
            if x.isnumeric():
                print(int(x))
                return func(x)
            else:
                raise ValueError('Yor integer string is not integer!')
        return converter
    @staticmethod
    def to_str(func):
        def converter(*args, **kwargs):
            x = args[0]
            x = str(x)
            return func(x)
        return converter
    @staticmethod
    def to_bool(func):
        def converter(*args, **kwargs):
            if type(args[0]) == bool:
                return func(args[0])
            else:
                raise ValueError('Yor boolean expression is not boolean!')
        return converter
    @staticmethod
    def to_float(func):
        def converter(*args, **kwargs):
            if type(args[0]) == float:
                return func(args[0])
            else:
                raise ValueError('Yor float number is not float!')
        return converter


@TypeDecorators.to_float
# @TypeDecorators.to_bool
# @TypeDecorators.to_int
# @TypeDecorators.to_str
def do_something(string:str):
    return string
###################################
#---------convert all to integer-------


x = do_something(1.2)
print(x)

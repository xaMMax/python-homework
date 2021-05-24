import re

class TypeDecorators:
    def __init__(self, *args):
        self.args = args

    @staticmethod
    def to_int(func):
            def converter(*args, **kwargs):
                x = (args[0])
                try:
                    x = int(re.sub('\D','', x))
                    return func(x)
                except ValueError:
                    return f'Yor integer string is not integer! {func}'
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
            try:
                bool(args)
                return func(args)
            except ValueError:
                return f'Yor boolean string is not boolean! {func}'
        return converter


    @staticmethod
    def to_float(func):
        def converter(*args, **kwargs):
            x = (args[0])
            try:
                x = re.findall('\d+\.\d+', x)
                return func(x)
            except ValueError:
                return f'Yor integer string is not integer! {func}'
        return converter





# @TypeDecorators.to_int
@TypeDecorators.to_str
def do_something(string:str):
    return string
###################################
#---------convert all to integer-------
# x = do_something('3, 3')
# print(x)
# print(type(x))
# a = x + 3
# print(a)
###################################
#---------convert to string-------
# x = do_something(21.651)
# print(x)
# print(type(x))






@TypeDecorators.to_bool
def do_nothing(string:str):
    return string

x = do_nothing(12)
print(x)


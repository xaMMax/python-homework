import re

from pythonds.basic.stack import Stack


def del_symbols(symbol_string):
    symbol_string = re.sub('[A-Za-z0-9]', '', symbol_string)
    return parChecker(symbol_string)


def parChecker(symbol_string):


    s = Stack()
    balanced = True
    index = 0
    while index < len(symbol_string) and balanced:
        symbol = symbol_string[index]
        if symbol == "(" or symbol == "{" or symbol == "[":
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                s.pop()

        index = index + 1

    if balanced and s.isEmpty():
        return True, symbol_string
    else:
        return False, symbol_string

print(del_symbols('(sdfs((sdfasdf)sdfas))'))
print(del_symbols('((asdf)'))
print(del_symbols('[[sdfsad]]'))
print(del_symbols('[[sdfas]'))
print(del_symbols('{{sdfs}}'))
print(del_symbols('{{sdfs}'))

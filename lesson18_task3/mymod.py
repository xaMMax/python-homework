import sys, os, fnmatch

def find(*args, path = '/home'):
    result = []
    for root, dirs, files in os.walk(path):
        for name in files:
            if fnmatch.fnmatch(name, *args):
                result.append(os.path.join(root, name))
    return result


def count_lines(name: str):
        f = open(name, 'r')
        lines = f.readlines()
        return len(lines)


def count_chars(name: str):
        f = open(name, 'r')
        result = f.read()
        return len(result)


def test(name: str):
    print(f'Your file has\n{count_lines(name)} lines,\n{count_chars(name)} chars')


try:
     test((find(sys.argv[1])[0]))
except IndexError:
    try:
        name = input('Input filename without PATH, i`m find file automatically ')
        test((find(name)[0]))
    except IndexError:
            exit('I can`t find your file, check all and try again.')



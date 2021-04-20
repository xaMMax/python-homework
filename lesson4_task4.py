import random
a = random.randint(1, 5)
b = random.randint(1, 5)
print('what result of a**b?', a, b)


def powf():
    result = a**b
    return result


i = input('type some number ')
if i.isdigit() and int(i) == powf():
    print('You WIN! My result is ', powf(), '' + 'and your result is ', i)
else:
    print('You Lose! My result is ', powf())

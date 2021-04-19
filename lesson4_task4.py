import math
import random
a = random.randint(1, 5)
b = random.randint(1, 5)
print('what result of a**b?', a, b)
def powF():
    result = a**b
    return result
i = int(input('type some '))
if i == powF():
    print('You WIN! My result is ', powF(),'' + 'and your result is ', i)
else:
    print('You Lose! My result is ', powF(),'' + 'and your result is ', i)
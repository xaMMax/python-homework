# Words combination

import random

your_string = input("type your string here ")
your_string = list(your_string)
for times in range(5):
    random.shuffle(your_string)
    shuffle_string = ''.join(your_string)
    print(shuffle_string)

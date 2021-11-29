# guessing game
import random

random_number = random.randint(1, 10)
user_number = input('What number I was guessed, from 1 to 10?\n')
if random_number == int(user_number):
    print(f'well done, your number is {user_number}, i guessed {random_number}')
else:
    print(f'try again, your number is {user_number}, my number is {random_number}')


import random  # import module random
i = 0           # use i variable starts from 0
yourString = input('Input your string ')    # use input method for input some string
if len(yourString) < 2:
    print('Please type string again ')  # prompt to type string again if user types <2 symbols
else:
    while i < 5:    # use loop for generated 5 prints
        result1 = ''.join((random.sample(yourString, len(yourString))))    # use join and random method for do random string
        i = i + 1   # use i + 1 for good loop
        print(" Random generated string x5: ", result1)  # print new string 5 times

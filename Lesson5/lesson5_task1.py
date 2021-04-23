import random  # import random module

listNum = []  # create list
i = 0  # i for use in while loop
while i < 10:  # while loop
    randNum = round(random.random(), 2) # generate random float again and again with round of 2 decimal places
    #  print(randNum)
    listNum.extend([randNum])  # extend our list by new random number
    #  print(listNum)
    i += 1  # our loop i
print('Our list of random numbers is ', listNum, '\nand the largest number in this list = ', max(listNum))  # use print for users


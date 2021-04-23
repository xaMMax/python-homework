import random

randNum = round(random.random(), 2)
listNum = [randNum, ]
i = 0
while i < 10:
    randNum = round(random.random(), 2)
    #  print(randNum)
    listNum.extend([randNum])
    #  print(listNum)
    i += 1
print('our list of random numbers is ', listNum, 'and the largest number in this list = ', max(listNum))


import random  # import random module

list1 = []  # create list
list2 = []  # create second list
i = 0  # i for use in while loop
while i < 10:  # while loop
    randNum0 = random.randint(1, 10)  # generate random integer 10 times for first list
    randNum1 = random.randint(1, 10)  # generate random integer 10 times for second list
    list1.append(randNum0)  # extend our first list by new random integer
    list2.append(randNum1)  # extend our second list by new random integer
    i += 1  # our loop i
list1 = set(list1) | set(list2)  # use union sets
print('Our list of with exclusive numbers is\n', list(list1))  # use list for carry out lesson task



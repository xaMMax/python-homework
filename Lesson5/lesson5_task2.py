import random  # import random module

list1 = []  # create list
list2 = []  # create second list
i = 0  # i for use in while loop
while i < 10:  # while loop
    randNum0 = random.randint(1, 10)  # generate random integer 10 times for first list
    randNum1 = random.randint(1, 10)  # generate random integer 10 times for second list
    list1.extend([randNum0])  # extend our first list by new random integer
    list2.extend([randNum1])  # extend our second list by new random integer
    i += 1  # our loop i
print('We have list1, and list2 with random integers\n', list1, '\n', list2)
list1.extend(list2)  # make 2 lists in one, extend first list by second
print('Our new list of list1 and list2\n', list1)  # print our new list for watch what we do
list1 = set(list1)  # use set for get exclusive numbers in our list
print('Our list of with exclusive numbers is\n', list(list1))  # use list for carry out lesson task

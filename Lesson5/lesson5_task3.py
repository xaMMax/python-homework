list0 = list(range(1, 101))  # create list with range from 1 to 100
print('We have some list with range from 1 to 100\n',list0)
list1 = []  # create list for our finish result
i = 1  # use favorite i
while i < 100:  # use loop with condition length of list
    if list0[i] % 7 == 0 and list0[i] % 5 != 0:  # if condition
        list1.append(i + 1)  # extend new list
        # print(list1)  # print the checklist
    i += 1  #
print('After some manipulation we have list what contains numbers \nthat are divisible by 7 and not divisible by 5\n', list1)  # print result list

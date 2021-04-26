def check_count_in_dict(m):  # create function
    count = {}  # create a dict
    for c in m:  # use for loop
       count[c] = m.count(c)  # fill our dictionary
    return count  # return dict


m = input('Input text here: ')  # create string
m = m.strip(' ')  # delete spaces in start and finish of the string
m = m.split()  # use split for crate some list
print('Your dictionary is:\n', check_count_in_dict(m))  # print our result

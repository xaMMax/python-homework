m = input('Input text here: ')  # create string
m = m.strip(' ')  # delete spaces in start and finish of the string
m = m.split(' ')  # use for create list
d = dict.fromkeys(m)  # create dict from our list with keys 'm' and values 'None'
i = 0
for key in d:  # for len d.keys
    d[key] = [i]  # create values for our dictionary
    i += 1
print('Your dictionary is:\n', d)  # print dictionary with unique words and values of occurrences

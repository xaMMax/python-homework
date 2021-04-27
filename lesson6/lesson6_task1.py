m = input('Input text here: ')  # create string
m = m.split()  # use split for crate some list
count = {i: m.count(i) for i in m if i != ''}  # use list comprehension for create dict
print('Your dictionary is:\n', count)

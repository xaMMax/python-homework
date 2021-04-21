name = input('Hello, please input your name: ')  # input name
age = int(input('and, please input your age: '))  # input age
if 0 < age < 101:  # if statement for correct age
    print('Greetings ' + name + ', next birthday you will be ' + str(int(age + 1)) + ' years!')  # print result
else:
    print('Who are you alien? -_-' + ' on your next birthday you’ll be ' + str(int(age + 1)) + ' years! -_-')  # print result if age is incredible

name = input('Hello, please input your name ') #input name
age = int(input('Hello, please input your age ')) #input age
if 0 < age < 101: #if statement for correct age
    print('Hello ' + name + ', on your next birthday you’ll be ' + str(int(age + 1)) + ' years!') #print result
else:
    print('Who are you alien? -_-' + ' on your next birthday you’ll be ' + str(int(age + 1)) + ' years!') #print result if age is incredible

import random                       # import random module
compNumber = random.randint(1,10)   # generate random number
# print(compNumber)                   # some print 8)
name = input('Please input your name ')  # input gamer name
print('Hello ' + name + ' nise to see you in my game') if len(name) >=1 and name != ' ' else print('Sorry but name cant be empty')  # ternar operator for check length of name and print it
nameNumber = int(input('Can you guess my generated number? '))  # input gamers number
if nameNumber == compNumber:  # if statement for compare both numbers
    print('Congratulations you are guess my secret number (my number is ' + str(compNumber) + ')')  # print congratulations if if is true
else:
    while nameNumber != compNumber:  # if if is false go to loop for guess right number
        print('Wrong number try again')
        nameNumber = int(input('next number '))
        if nameNumber == compNumber:
            print('Congratulations you are guess my secret number (my number is ' + str(compNumber) + ')')
        else:
            continue

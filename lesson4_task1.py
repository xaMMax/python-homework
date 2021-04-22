import random                       # import random module
compNumber = random.randint(1, 10)   # generate random number
# print(compNumber)                   # some print 8)
name = input('Please input your name ')  # input gamer name
print('Hello ' + name + ' nise to see you in my game') if len(name) >= 1 and name != ' ' else print('Sorry but name cant be empty')  # ternar operator for check length of name and print it
nameNumber = input('Can you guess my generated number? ')  # input gamers number
print('Your number is : ', nameNumber)
while True:
    if nameNumber.isdigit() and int(nameNumber) == compNumber:
        print('Congratulations you are guess my secret number (my number is ', compNumber, ')')  # print congratulations if if is true
        break  # end of loop if win
    else:
        print('Wrong number try again')  # print wrong message
        nameNumber = input('next number ')  # try to next number
        print('Your number is : ', nameNumber)

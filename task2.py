#1 variant
"""
phoneNum = input('Type your phone number ') #create a variable
if phoneNum.isdigit() and len(phoneNum) == 10: #this if check our var for include digit and have length of 10 numbers
    print(phoneNum) #returns phone number
else:
    print('ERROR: you don`t use numbers or incorrect length of number') #returns error message
"""
#2 variant

phoneNum = input('Type your phone number ')  # create a variable
if phoneNum.isdigit():  # if our variable is digital
    if len(phoneNum) == 10:  # if our variable is same length
       print(phoneNum)  # print phone number
    else:
            print('ERROR: your phone length is incorrect')  # print error message with error type
else:
    print('ERROR: you don`t use numbers')  # print error message with error type


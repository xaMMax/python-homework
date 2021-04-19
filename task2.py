#1 variant

"""
phoneNum = input('Type your phone number ') #create a variable
if phoneNum.isdigit() and len(phoneNum) == 10: #this if check our var for include digit and have length of 10 numbers
    print(phoneNum) #returns phone number
else:
    print('ERROR: you don`t use numbers or incorrect length of number') #returns error message
"""

#2 variant

'''
phoneNum = input('Type your phone number ')  # create a variable
if phoneNum.isdigit():  # if our variable is digital
    if len(phoneNum) == 10:  # if our variable is same length
       print('your phone number is: ' + phoneNum)  # print phone number
    else:
            print('ERROR: your phone length is incorrect')  # print error message with error type
else:
    print('ERROR: you don`t use numbers')  # print error message with error type
'''

#3 variant 'ternar operator'

phoneNum = int(input('''Type your phone number 
(note: phone number must contain 10 digits, without alphabet symbols)
:''')) # create a variable
print('your phone number is: ', phoneNum) if type(phoneNum) == int and len(str(phoneNum)) == 10 else print('error: phone number is incorrect')
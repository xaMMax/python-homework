phoneNumber = input('''Type your phone number 
(note: phone number must contain 10 digits, without alphabet symbols)
:''')  # use input method with int
print('your phone number is: ', phoneNumber) if phoneNumber.isdigit() and len(str(phoneNumber)) == 10 else \
    print('error: phone number is incorrect')  # use syntactic sugar to check for correct phone number

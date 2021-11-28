yourString = input('Please type your string here ')  # input sample string
if len(yourString) >= 2:  # use function len for compare and go to next step
    expString = yourString[:2] + yourString[-2:]  # use indexing for doing lesson
    print('your string is ' + yourString, 'and expected result is ' + expString)  # print our conditions on screen
else:
    print('Please restart me and input correct string, more than 2 symbols')  # if yourStr len less than 2

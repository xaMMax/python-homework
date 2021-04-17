yourStr = input('Please type your string here ') # input sample string
if len(yourStr) >= 2:                            # use function len for compare and go to next
    expString = yourStr[:2] + yourStr[-2:]       # use indexing for doing lesson
    print('your string is ' + yourStr, 'and expected result is ' + expString) #print our condidions on screen
else: print('empty string')     # if yourStr len less than 2

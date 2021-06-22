myName = 'maksym'                                #create variable
inpName = input('Type your Name ')               #input name for compare
if inpName.lower() == myName:                    #if our input = variable ->
    print(True)                                  #print true
else:
    print('ERROR: your name is not maksym goodbye amigo')   #print error message with error type amigo
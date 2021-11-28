myName = 'maks'  # create variable
inpName = input('Type your Name ')  # input name for compare
if inpName.lower() == myName:  # if your input = variable ->
    print(True, 'Welcome amigo!')  # print true, and welcome text
else:
    print('ERROR: your name is not "Maks" goodbye amigo.')  # print error message

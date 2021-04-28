def make_operation(x='', *args):  # define the function called make_operation
    result = 1  # use variable for use in operatoins
    if x == '*':  # if else statement for choice the type of operation
        for i in args:
            result *= i
            print(result)
    elif x == '+':
        result = sum(args)
        print(result)
    elif x == '-':
        result = args[0] - args[1]
        print('Sorry at this time you can subtract only two arguments', args[0], 'and', args[1],'resultis',  result)
    else:
        print('it is bad func')

    return  # return result of operations


make_operation('+', 5, 6, 2)  # call the function


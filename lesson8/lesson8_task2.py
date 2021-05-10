def calculator():  # call the function
    try:  # try except construction
        a = int(input('Input first number\na= '))  # user input number called a
        b = int(input('Input second number\nb= '))  # user input number called b
        print('Result of (a power 2) divided by b is', (a*a) / b)  # print result if our user correctly input variables
    except ValueError:  # use value error exception for pull out all non digits elements
        print('Value error, use digits')  # print type of except for user
        calculator()  # recall function for repeat users input
    except ZeroDivisionError:  # use zero division error exception because we can not divide by zero
        print('ZeroDivision Error, you can`t divide by zero')  # print type of except for user
        calculator()  # recall function for repeat users input
    return


calculator()

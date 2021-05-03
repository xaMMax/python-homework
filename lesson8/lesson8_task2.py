def calculator():
    a = input('Input first number\na= ')
    b = input('Input second number\nb= ')
    try:
        a.isdigit()
        b.isdigit()
        a = int(a)
        b = int(b)
        result = (a*a) / b
        print('Result of (a power 2) divided by b is', result)
    except ValueError:
        print('Value error, use digits')
        calculator()
    except ZeroDivisionError:
        print('ZeroDivision Error, you can`t divide by zero')
        calculator()
    return


calculator()

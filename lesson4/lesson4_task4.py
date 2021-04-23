import random  # import random module
a = random.randint(1, 5)  # create variable a with randint method
b = random.randint(1, 5)  # create variable b with randint method
print('What is the result of raising "a" to the power of "b" if "a"=', a, 'and b=', b)  # print the condition of task
result = a ** b  # raise to the power
i = input('Type your answer: ')  # use input for user answer
if i.isdigit() and int(i) == result:  # if statement for checking numbers and user answer
    print('You WIN! My result is ', result, '' + 'and your result is ', i)  # print if user win
else:
    print('You Lose! My result is ', result)  # print if user lose

from re import *

def decorator_for_email_class(cls):
        def validate(*args):
            print(args[0])
            pattern = compile('(^|\s)[-a-z0-9_.]+@([-a-z0-9]+\.)+[a-z]{2,6}(\s|$)')
            is_valid = pattern.match(str(args[0]))
            if is_valid:
                print('правильный email:', is_valid.group())
                            # объект is_valid содержит 3 метода
                        # print('методы: start:', is_valid.start(), 'end:', is_valid.end(), 'group:', is_valid.group())
            else:
                print('неверный email! введите email...\n')
            return cls(*args)
        return validate


@decorator_for_email_class
class EmailValid:
    def __init__(self, email):
        self.email = email


newmail = EmailValid('asfsdf@gmail.com')

print(newmail.email)

newmail2 = EmailValid('dfgdgdrgeg2@@@')


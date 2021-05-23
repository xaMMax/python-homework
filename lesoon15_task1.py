from re import *
class EmailValid:
    def __init__(self, *args):
        self.validate(*args)

    def validate(*args):
        pattern = compile('(^|\s)[-a-z0-9_.]+@([-a-z0-9]+\.)+[a-z]{2,6}(\s|$)')
        address = input('inter you email address:')
        is_valid = pattern.match(address)
        if is_valid:
            print('правильный email:', is_valid.group())
                # объект is_valid содержит 3 метода
            # print('методы: start:', is_valid.start(), 'end:', is_valid.end(), 'group:', is_valid.group())
        else:
            print('неверный email! введите email...\n')



new_mail = EmailValid()
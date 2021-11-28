import logging


class CustomException(Exception):

    def __init__(self, msg = ''):
        self.msg = msg
        super().__init__(self.msg)
        logging.basicConfig(filename='logs.txt', filemode='a')
        logging.exception(msg)

    def __str__(self):
        return self.msg


a = int(input('input int '))
b = 4
try:
    if a < b:
        raise CustomException(f'number {a} is too less ')
    elif a > b:
        raise CustomException(f'number {a} is too more ')
except Exception as e:
    print(f'bad number {e}')

import json
from collections import OrderedDict


class Abonent:
    def __init__(self, name, second_name, phone_number, city_state):
        self.name = name
        self.second_name = second_name
        self.phone_number = phone_number
        self.city_state = city_state






choice = input(''
    'If you want add the contact press 1\nIf you want find by name press 2\nIf you want find by second name press 3\n'
    'If you want find by full name press 4\nIf you want find by phone number press 5\nIf you want find by Sity press 6\n'
    'If you want delete by number press 7\nIf you want renew by number press 8\n')

def menu(choice):
    if choice == '1':
        # contact_dict = dict(name= input('name \n'), second_name= input('second name \n'),
        #                     number= input('phone number \n'), state= input('state or country \n'))
        new_abonent = Abonent(name=input('name'),second_name=input('second name '),
                              phone_number=input('phone number '), city_state=input('city '))
        with open('phonebook.json', 'a') as f:
            f.write(str(new_abonent.__dict__) + '\n')
            f.close()
    elif choice == '2':
        target = input('Enter search name ')
        with open('phonebook.json', 'r') as f:
            data = OrderedDict(json.load(f))
            print(data)






menu(choice)
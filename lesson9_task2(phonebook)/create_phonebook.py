import json
choice = input(''
    'Если вы хотите создать или добавить контакт нажмите 1\nДля поиска по имени нажмите 2\nДля поиска по фамилии нажмите 3\n'
    'Для поиска по полному имени нажмите 4\nДля поиска по номеру телефона 5\nДля поиска по стране или штату нажмите 6\n'
    'Удалить контакт по номеру нажмите 7\nОбновить контакт по номеру телефона нажмите 8\n')



def create_abonent():
    abonent = {'name': input('Имя '), 'second_name': input('Фамилия '),
               'phone_number': input('Номер телефона '), 'sity': input('страна или штат ')}
    return abonent

def load_file(file):
    with open(file) as f:
        file = json.load(f)
    return file

def dump_to_file(file, data):
    with open(file, 'w') as f:
        json.dump(data, f, indent=2)



def menu():
    default_book = ['Phonebook']

#######################
# add abonent         #
    if choice == '1':
        try:
            with open('phonebook.json') as f:
                data = json.load(f)
                with open('phonebook.json', 'w') as f:
                    data.append(create_abonent())
                    json.dump(data, f, indent=3)
        except:
            with open('phonebook.json', 'w') as f:
                default_book.append(create_abonent())
                json.dump(default_book, f, indent=3)


##################
#    find by name  #
    if choice == '2':
        find_item = input('Введите имя контакта ')
        try:
            with open('phonebook.json') as f:
                data = json.load(f)
                for items in data[1:]:
                    if items['name'] == find_item:
                        print(f"Контакт найден \nИмя {items['name']}\nФамилия {items['second_name']}\n"
                              f"Тел. номер {items['phone_number']}\nСтрана/штат {items['sity']}")
                        break
                    else:
                        continue
        except:
            print('Ничего не найдено')
##################
#    find by second name  #
    if choice == '3':
        find_item = input('Введите фамилию контакта ')
        try:
            with open('phonebook.json') as f:
                data = json.load(f)
                for items in data[1:]:
                    if items['second_name'] == find_item:
                        print(f"Контакт найден \nИмя {items['name']}\nФамилия {items['second_name']}\n"
                              f"Тел. номер {items['phone_number']}\nСтрана/штат {items['sity']}")
                        break
                    else:
                        continue
        except:
            print('Ничего не найдено')
##################
#    find by full name  #
    if choice == '4':
        find_item = input('Введите имя и фамилию контакта ').split()
        try:
            with open('phonebook.json') as f:
                data = json.load(f)
                for items in data[1:]:
                    if items['name'] == find_item[0] and items['second_name'] == find_item[1]:
                        print(f"Контакт найден \nИмя {items['name']}\nФамилия {items['second_name']}\n"
                                f"Тел. номер {items['phone_number']}\nСтрана/штат {items['sity']}")
                        break
                    else:
                        continue
        except:
            print('Ничего не найдено')
##################
#    find by number  #
    if choice == '5':
        find_item = input('Введите номер контакта ')
        try:
            with open('phonebook.json') as f:
                data = json.load(f)
                for items in data[1:]:
                    if items['phone_number'] == find_item:
                        print(f"Контакт найден \nИмя {items['name']}\nФамилия {items['second_name']}\n"
                              f"Тел. номер {items['phone_number']}\nСтрана/штат {items['sity']}")
                        break
                    else:
                        continue
        except:
            print('Ничего не найдено')
##################
#    find by country  #
    if choice == '6':
        find_item = input('Введите страну контакта ')
        try:
            with open('phonebook.json') as f:
                data = json.load(f)
                for items in data[1:]:
                    if items['sity'] == find_item:
                        print(f"Контакт найден \nИмя {items['name']}\nФамилия {items['second_name']}\n"
                              f"Тел. номер {items['phone_number']}\nСтрана/штат {items['sity']}")
                    else:
                        continue
        except:
            print('Ничего не найдено')
##################
#    delete by phone number  #
    if choice == '7':
        find_item = input('Введите номер контакта ')
        try:
            with open('phonebook.json') as f:
                data = json.load(f)
                for items in data[1:]:
                    if items['phone_number'] == find_item:
                        print(f"Контакт \n  Имя {items['name']}\n  Фамилия {items['second_name']}\n  "
                              f"Тел. номер {items['phone_number']}\n  Страна/штат {items['sity']}\nудален")
                        data.remove(items)
                        with open('phonebook.json', 'w') as f:
                            json.dump(data, f, indent=3)
                        break
                    else:
                        continue
        except:
            print('Ничего не найдено')
##################
#    edit by phone number #
    if choice == '8':
        find_item = input('Введите номер контакта ')
        try:
            with open('phonebook.json') as f:
                data = json.load(f)
                for items in data[1:]:
                    if items['phone_number'] == find_item:
                        print(f"Контакт найден \nИмя {items['name']}\nФамилия {items['second_name']}\n"
                              f"Тел. номер {items['phone_number']}\nСтрана/штат {items['sity']}")
                        data.remove(items)
                        with open('phonebook.json', 'w') as f:
                            data.append({'name': input('Новое имя '), 'second_name': input('Новая фамилия '),
                                            'phone_number': find_item, 'sity': input('Новые страна или штат ')})
                            json.dump(data, f, indent=3)
                        break
                    else:
                        continue
        except:
            print('Ничего не найдено')


menu()
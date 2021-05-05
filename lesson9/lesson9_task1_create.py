
string0 = ('Hello file world!\n')
file_path = '/home/maks/PycharmProjects/python-homework/lesson9/myfile.txt'
with open(file_path, 'w') as file_object:
    file_object.write(string0)

file_path = '/home/maks/PycharmProjects/python-homework/lesson9/myfile.txt'

with open(file_path) as file_object:
    string0 = file_object.read()
print(string0)
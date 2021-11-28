class MyClass:
    def __init__(self, something):
        self.something = something

    def __getitem__(self, index):
        print('Calls Getitem')
        return self.something[index]

listof = MyClass([1, 2, 3, 4])


for i in listof:
    print(i)

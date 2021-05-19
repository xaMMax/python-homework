class Person():
    fName = None
    sName = None
    age = None

    def __init__(self, firstName, secondName, myage):
        self.fName = firstName
        self.sName = secondName
        self.age = myage

    def talk(self):
        print(f'Hello, my name is {self.fName} {self.sName}, and i am {self.age} years old.')


myname = Person('Carl', 'Johnson', 26)
myname.talk()


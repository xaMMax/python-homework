class Person:

    def __init__(self, name, age, doing, who):
        self.name = name
        self.age = age
        self.doing = doing
        self.who = who

    def personName(self):
        return f'My name is {self.name} and i am a {self.who}'

    def whatDoing(self):
        return f'I am a {self.who} and i am {self.doing} '

    def age_t(self):
        return f'My age is {self.age}'

class Teacher(Person):

    def __init__(self, name, age, doing, salary, who):
        self.salary = salary
        super().__init__(name, age, doing, who)

    def salary_t(self):
        return f'My salary is {self.salary}'

class Student(Person):
    def __init__(self, name, age, doing, who):
        super().__init__(name, age, doing, who)


vasulStudent = Student('Vasul', 22, 'studying', 'student')
svetaTeacher = Teacher('Sveta', 24, 'teaching', 15000, 'teacher')

print(vasulStudent.personName())
print(vasulStudent.whatDoing())
print(vasulStudent.age_t())


print(svetaTeacher.whatDoing())
print(svetaTeacher.salary_t())
print(svetaTeacher.age_t())
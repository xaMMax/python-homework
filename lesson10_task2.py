class Dog():
    age_factor = 7

    def __init__(self, age):
        self.age = age

    def human_age(self):
        return self.age_factor * self.age


newdog = Dog(10)
print(newdog.human_age())
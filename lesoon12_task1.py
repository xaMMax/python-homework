class Animal:
    def __init__(self, name, voice):
        self.name = name
        self.voice = voice

    def talk(self):
        print(f'{self.name} says {self.voice}')


class Dog(Animal):
    def talk(self):
        super().talk()
        print(f'{self.name} can also seating and {self.voice}')


class Cat(Animal):
    pass


abracadabra = Dog('abracadabra', 'woof-woof')
abracadabra.talk()

murzik = Cat('murzik', 'meow')
murzik.talk()


def simple_universal_function(a, b):
    Animal.talk(a)
    Animal.talk(b)


simple_universal_function(abracadabra, murzik)

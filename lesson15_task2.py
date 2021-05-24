class Boss:
    def __init__(self, id_:int, name:str, company:str):
        self.id = id_
        self.name = name
        self.company = company
        self.workers = []
        pass
    def add_workers(self, *args):
        self.workers.append(args)
        return self.workers

    def __repr__(self):
        return f'The {self.name}'

class Worker:
    def __init__(self, id_:int, name:str, company:str, __boss: Boss):
        self.id = id_
        self.name = name
        self.company = company
        self.__boss = __boss
        pass
    @property
    def boss(self):
        return self.__boss
    @boss.setter
    def boss(self, boss_is):
        self.__boss = boss_is
        return


    def __repr__(self):
        return f'Worker {self.name}, with id #{self.id}, worked in {self.company} boss is {self.__boss}'


new_boss = Boss(1, 'Max', 'IT~LSD')
worker1 = Worker(11, 'Vasya', 'IT~LSD', new_boss.name)
worker2 = Worker(12,'Nigga', 'IT~LSD', new_boss.name)
worker3 = Worker(13,'Chiny', 'It~LSD', new_boss.name)

new_boss.add_workers(worker1)
new_boss.add_workers(worker2)
new_boss.add_workers(worker3)

worker1.__boss = 'Some Vasiliy'
worker2.__boss = new_boss.name

print(worker1.__boss)
print(worker2.__boss)
print(worker3)


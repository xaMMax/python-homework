class Boss:
    def __init__(self, id_:int, name:str, company:str):
        self.id = id_
        self.name = name
        self.company = company
        self.workers = []
    def add_workers(self, workr):
        if isinstance(workr, Worker):
            self.workers.append(workr)
            return self.workers
        else:
            print(f'you cant add non workers object {workr}')
    def __repr__(self):
        return f'The {self.name}'


class Worker:
    def __init__(self, id_:int, name:str, company:str, boss_is=Boss):
        self.id = id_
        self.name = name
        self.company = company
        self.__boss = boss_is
    @property
    def boss(self):
        return self.__boss
    @boss.setter
    def boss(self, boss_is):
        if isinstance(boss_is, Boss):
            self.__boss = boss_is
        else:
            print(f'you cant add non boss object')
    def __repr__(self):
        return f'Worker {self.name}, with id #{self.id}, worked in {self.company} boss is {self.__boss}'


new_boss = Boss(1, 'Max', 'IT~LSD')
worker1 = Worker(11, 'Vasya', 'IT~LSD')
worker2 = Worker(12,'Nigga', 'IT~LSD')
worker3 = Worker(13,'Chiny', 'It~LSD')


worker1.__boss = new_boss
new_boss.add_workers(worker1)


print(worker1.__boss)
print(new_boss.workers)
print(new_boss)

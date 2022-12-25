class Boss:
    def __init__(self, id_: int, name: str, company: str):
        self.id = id_
        self.name = name
        self.company = company
        self.workers = []

    def __str__(self):
        return self.name

    def add_worker(self, worker):
        if isinstance(worker, Worker):
            self.workers.append(worker)

    def display_workers(self):
        print(f'{self.name} has following workers:')
        for worker in self.workers:
            print(worker.name)


class Worker:

    def __init__(self, id_: int, name: str, company: str, boss: Boss):
        self.id = id_
        self.name = name
        self.company = company
        self.__boss = boss

    def __str__(self):
        return f'This is a worker {self.name} and his boss is {self.boss}.'

    @property
    def boss(self):
        return self.__boss.name

    @boss.setter
    def boss(self, new_boss):
        if isinstance(new_boss, Boss):
            self.__boss = new_boss
            print(f'{self.name} has a new boss {self.boss}')
            new_boss.add_worker(self)
        else:
            raise ValueError('Object has to be a "Boss" type.')




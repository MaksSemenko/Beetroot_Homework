class Person:
    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age


    def greeting(self):
        print(f"Hello, my name is {self.firstname} {self.lastname}, I'm {self.age} years old"
              f" and I'm an alcoholic")


person_1 = Person('Maks', 'Semenko', 25)
person_1.greeting()

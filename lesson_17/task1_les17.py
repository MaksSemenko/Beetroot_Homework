class Animal:
    def talk(self):
        raise NotImplementedError('This method should be defined in subclasses!')


class Dog(Animal):
    def talk(self):
        print('woof woof')


class Cat(Animal):
    def talk(self):
        print('meow')


def what_does_the_animal_say(x):
    x.talk()

cat = Cat()
dog = Dog()
what_does_the_animal_say(cat)
what_does_the_animal_say(dog)

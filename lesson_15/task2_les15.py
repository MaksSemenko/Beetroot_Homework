class Dog:
    age_factor = 7

    def __init__(self, age):
        self.age = age

    @property  # There is no need to use it, but just wanted to practise this
    def human_age(self):
        return self.age * Dog.age_factor


dog_1 = Dog(7)
print(dog_1.human_age)

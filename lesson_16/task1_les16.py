class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        pass

    def greeting(self):
        print(f'Hello my name is {self.first_name} {self.last_name}')


class Student(Person):
    def __init__(self, first_name, last_name, age, subject, mark):
        super().__init__(first_name, last_name, age)
        self.subject = subject
        self.mark = mark

    def my_mark(self):
        if self.mark < 10:
            print(f"I've got {self.mark} for {self.subject}. My mum will kill me!")
        else:
            print(f"I've got {self.mark} for {self.subject}. I am a genius!")


class Teacher(Person):
    def __init__(self, first_name, last_name, age, salary):
        super().__init__(first_name, last_name, age)
        self.salary = salary

    def my_salary(self):
        if self.salary < 10_000:
            print(f"I've got {self.salary} dollars this month. I should have learned Python")
        else:
            print(f"I've got {self.salary} dollars this month. God bless Pedagogical University")


student = Student('Victor', 'Petrenko', 13, 'Biology', 3,)
teacher = Teacher('Maria', 'Salo', 59, 11_000)
student.greeting()
student.my_mark()
teacher.greeting()
teacher.my_salary()

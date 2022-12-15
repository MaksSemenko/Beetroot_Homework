class Mathematician:
    def square_nums(self, x):
        return [i**2 for i in x]

    def remove_positives(self, x):
        return [i for i in x if i < 0]

    def filter_leaps(self, x):
        return [i for i in x if i % 4 == 0]


m = Mathematician()
print(m.square_nums([7, 11, 5, 4]))
print(m.remove_positives([26, -11, -8, 13, -90]))
print(m.filter_leaps([2001, 1884, 1995, 2003, 2020]))

def func_1(x):
    def func_2(y):
        return y ** x
    return func_2


general_func = func_1(3)
print(general_func(2))

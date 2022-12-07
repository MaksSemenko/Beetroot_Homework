def my_func1():
    my_int = 1
    my_str = 'I need more electricity'
    my_list = [1, 2, 1, 2, 3]


def my_func2():
    my_int = 1
    my_str = 'I need more electricity'
    my_list = [1, 2, 1, 2, 3]
    my_dict = {'love': 'hate', 'freedom': 'slavery'}
    my_set = {1, 2, 3}


def counter_of_loc_var(func):
    print(func.__code__.co_nlocals)


counter_of_loc_var(my_func1)
counter_of_loc_var(my_func2)

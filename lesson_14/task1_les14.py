from functools import wraps

def logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f'Function {func.__name__} was called with arguments {args}!')
    return wrapper


@logger
def add(x, y):
    return x + y


@logger
def square_all(*args):
    return [arg ** 2 for arg in args]


add(1, 2)
square_all(1, 2, 3, 4, 5)

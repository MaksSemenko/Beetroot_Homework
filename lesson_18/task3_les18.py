from functools import wraps

class TypeDecorators:

    @staticmethod
    def to_int(func):
        @wraps(func)
        def call_int(*args, **kwargs):
            print('Converted to int')
            try:
                x = func(*args, **kwargs)
                return int(x)
            except ValueError:
                raise ValueError('Inappropriate argument was passed to function')
        return call_int

    @staticmethod
    def to_str(func):
        @wraps(func)
        def call_str(*args, **kwargs):
            print('Converted to str')
            try:
                x = func(*args, **kwargs)
                return str(x)
            except ValueError:
                raise ValueError('Inappropriate argument was passed to function')
        return call_str

    @staticmethod
    def to_bool(func):
        @wraps(func)
        def call_bool(*args, **kwargs):
            print('Converted to bool')
            try:
                x = func(*args, **kwargs)
                return bool(x)
            except ValueError:
                raise ValueError('Inappropriate argument was passed to function')
        return call_bool

    @staticmethod
    def to_float(func):
        @wraps(func)
        def call_float(*args, **kwargs):
            print('Converted to float')
            try:
                x = func(*args, *kwargs)
                return float(x)
            except ValueError:
                raise ValueError('Inappropriate argument was passed to function')
        return call_float


@TypeDecorators.to_int
def do_nothing(string: str):
    return string


@TypeDecorators.to_bool
def do_something(string: str):
    return string


print(do_nothing('25'))
print(do_something('True'))
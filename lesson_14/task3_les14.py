def arg_rules(type_, max_length, contains):
    def wrapper(func):
        def inner_wrapper(name):
            if type(name) is type_ and len(name) <= max_length and \
                    contains[0] in name and contains[1] in name:
                print(func(name))
            else:
                return False
        return inner_wrapper
    return wrapper


@arg_rules(type_=str, max_length=15, contains=['05', '@'])
def create_slogan(name) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"


create_slogan('johndoe05@gmail.com')
create_slogan('S@SH05')

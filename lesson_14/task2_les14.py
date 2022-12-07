def stop_words(my_list):
    def wrapper(func):
        def inner_wrapper(name):
            some_string = func(name)
            for word in my_list:
                x = some_string.replace(word, '*')
                some_string = x
            print(x)
        return inner_wrapper
    return wrapper


@stop_words(['pepsi', 'BMW'])
def create_slogan(name) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"


create_slogan("Steve")

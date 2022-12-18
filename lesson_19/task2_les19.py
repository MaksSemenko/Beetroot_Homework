def in_range(*args):
    lst = []
    if len(args) == 1: # If there is one argument, it means it must be "stop" argument, starting from 0 and step is 1.
        number = 0
        while number < args[0]:
            lst.append(number)
            number += 1
    elif len(args) == 2: # For two arguments, "classical" range function
        number = args[0]
        while number < args[1]:
            lst.append(number)
            number += 1
    elif len(args) == 3:  # For a positive step
        number = args[0]
        if args[0] < args[1]:
            while number < args[1]:
                lst.append(number)
                number += args[2]
        elif args[0] > args[1]:   # For a negative step
            while number > args[1]:
                lst.append(number)
                number += args[2]
    else:
        raise TypeError(f'range expected maximum 3 arguments, got {len(args)}')
    return lst

# Example with only one argument.
for i in in_range(10):
    print(i)
print('\n')

# Example with two arguments.
for i in in_range(1, 10):
    print(i)
print('\n')

# Example with step argument, and with negative step as well.
for i in in_range(100, -10, -10):
    print(i)

# Gives an error if there is no arguments.
# for i in in_range():
#     print(i)
# Gives an error if there is more than 3 arguments.
# for i in in_range(1, 10, 1, 1):
#     print(i)

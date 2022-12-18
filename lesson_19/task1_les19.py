def with_index(iterable, start=0):
    for item in iterable:
        yield start, item
        start += 1

# List to  test with_index function.
sides_of_the_world = ['North', 'South', 'East', 'West']

for i in with_index(sides_of_the_world):
    print(i)

for i, value in with_index(sides_of_the_world, 1):
    print(i, value)

# Dictionary to test with_index function.
opposites_dict = {'dusk': 'dawn', 'good': 'bad', 'summer': 'winter'}

for i in with_index(opposites_dict, 1):
    print(i)

for i, (k, v) in with_index(opposites_dict.items(), 1):
    print(i, k, v)

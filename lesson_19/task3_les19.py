class Counter:

    def __init__(self, low, high):
        self.__current = low
        self.__low = low
        self.__high = high
        self.__range = range(low, high)

    def __iter__(self):
        return self

    def __getitem__(self, index):
        result = self.__range.__getitem__(index)
        if isinstance(index, slice):
            return list(result)
        return result

    def __next__(self):
        if self.__current > self.__high:
            raise StopIteration
        else:
            self.__current += 1
            return self.__current - 1

c = Counter(1, 10)
for i in c[1:10:2]:
    print(i)
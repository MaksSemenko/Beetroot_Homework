class MyOpen:
    counter = 0

    def __init__(self, file_name, method):
        self.file = open(file_name, method)

    def __enter__(self):
        MyOpen.counter += 1
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            with open('logging.txt', 'w') as log:
                log.write(f'{exc_type}\n')
        self.file.close()

with MyOpen('some_text.txt', 'w') as some_file:
    some_file.write('Test of customized context manager was successful!')
print(f'MyOpen context manager was used {MyOpen.counter} times')
# Case to test logging, for example AttributeError
# with MyOpen('some_text.txt', 'w') as some_file:
#     some_file.writes('Test of customized context manager was successful!')

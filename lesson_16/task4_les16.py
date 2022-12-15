class CustomException(Exception):
    def __init__(self, msg=''):
        super().__init__(msg)
        self.msg = msg
        with open('logs.txt', 'a+') as f:
            f.write(self.msg)


raise CustomException('Some error has occurred!\n')

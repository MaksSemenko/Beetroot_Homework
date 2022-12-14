class TVController:

    def __init__(self, list_of_channels):
        self.channels = list_of_channels
        self.counter = 0

    def first_channel(self):
        self.counter = 0
        return self.channels[0]

    def last_channel(self):
        self.counter = len(self.channels) - 1
        return self.channels[self.counter]

    def turn_channel(self, number):
        return self.channels[number-1]

    def next_channel(self):
        if self.channels[self.counter] == self.channels[-1]:
            self.counter = 0
        else:
            self.counter += 1
        return self.channels[self.counter]

    def previous_channel(self):
        if self.channels[self.counter] == self.channels[0]:
            self.counter = len(self.channels) - 1
        else:
            self.counter -= 1
        return self.channels[self.counter]

    def current_channel(self):
        return self.channels[self.counter]

    def is_exist(self, name):
        if type(name) == int:
            if name <= len(self.channels):
                return 'Yes'
            return 'No'
        elif type(name) == str:
            if name in self.channels:
                return 'Yes'
            return 'No'
        return 'Wrong input type, please try again'


CHANNELS = ['BBC', 'Discovery', 'TV1000']
controller = TVController(CHANNELS)
print(controller.first_channel())
print(controller.last_channel())
print(controller.turn_channel(1))
print(controller.next_channel())
print(controller.previous_channel())
print(controller.current_channel())
print(controller.is_exist(4))
print(controller.is_exist('BBC'))

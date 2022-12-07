class TVController:

    def __init__(self, list_of_channels):
        self.channels = list_of_channels
        self.default_channel = list_of_channels[0]

    def first_channel(self):
        return self.channels[0]

    def last_channel(self):
        return self.channels[-1]

    def turn_channel(self, number):
        return self.channels[number-1]

    def next_channel(self):
        if self.default_channel == self.channels[-1]:
            self.default_channel = self.channels[0]
        elif self.default_channel == self.channels[0]:
            self.default_channel = self.channels[1]
        elif self.default_channel == self.channels[1]:
            self.default_channel = self.channels[2]
        return self.default_channel

    def previous_channel(self):
        if self.default_channel == self.channels[0]:
            self.default_channel = self.channels[-1]
        elif self.default_channel == self.channels[1]:
            self.default_channel = self.channels[0]
        elif self.default_channel == self.channels[2]:
            self.default_channel = self.channels[1]
        return self.default_channel

    def current_channel(self):
        return self.default_channel

    def is_exist(self, name):
        if name in self.channels or name <= len(self.channels):
            return 'Yes'
        else:
            return 'No'


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

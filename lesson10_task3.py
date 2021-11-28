channels = ['BBC', 'Discovery', 'TV1000']

class TVController():

    def __init__(self):
        self.channels = channels

    def first_channel(self):
        print(self.channels[0])
        return self.channels[0]

    def last_channel(self):
        print(self.channels[-1])
        return self.channels

    def turn_channel(self, n):
        print(self.channels[n-1])
        return self.channels

    def next_channel(self):
        print(self.channels[+1])
        return self.channels

    def previous_channel(self):
        print(channels[0])

    def current_channel(self):
        print(channels[0])

    def is_exist(self, a):
        if a in channels:
            print(a)
        else:
            print('No')

    def __str__(self):
        return self.channels

new_control = TVController()
#
new_control.first_channel()
new_control.last_channel()
new_control.turn_channel(2)
new_control.next_channel()
new_control.previous_channel()
new_control.current_channel()
new_control.is_exist('Discovery')
new_control.is_exist(4)


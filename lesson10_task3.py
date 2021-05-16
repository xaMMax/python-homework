channels = ['BBC', 'Discovery', 'TV1000']

class TVController():

    def __init__(self, channels):
        self.channels = channels

    def first_channel(self):
        channel = channels[0]
        print(channel)

    def last_channel(self):
        channel = channels[-1]
        print(channel)

    def turn_channel(self, n):
        channel = channels[n-1]
        print(channel)
        return channel

    def next_channel(self):
        channel = channels
        print(channel[1])

    def previous_channel(self):
        print(channels[0])

    def current_channel(self):
        print(channels[0])

    def is_exist(self, a):
        if a in channels:
            print(channels.index(a), a)
        else:
            print('No')

new_control = TVController(channels)
#
# new_control.first_channel()
# new_control.last_channel()
# new_control.turn_channel(1)
# new_control.next_channel()
# new_control.previous_channel()
# new_control.current_channel()
new_control.is_exist('BBC')
new_control.is_exist(4)


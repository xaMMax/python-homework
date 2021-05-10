class TVController():
    channel = ['BBC', 'Discovery', 'TV1000']

    def __init__(self, channel):
        self.channel = channel

    def first_channel(self):
        print(self.channel[0])

    def last_channel(self):
        return self.channel[2]

    def turn_channel(self, n):
        return self.channel[n]

    def next_channel(self):
        return self.channel[:+1]
    def previon_cannel(self):
        return self.channel[-1:]
    def current_channel(self):
        pass
    def is_exist(self, a):
        pass

new_control = TVController
print(new_control.next_channel())
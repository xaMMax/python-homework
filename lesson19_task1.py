import logging
import time

class ConMan:
    def __init__(self, filename, mode):
        logging.basicConfig(level='DEBUG', filename='my_log.log')
        self.loger = logging.getLogger()
        #operation time
        sectime = time.time()
        self.time = time.ctime(sectime)
        # logger with counter
        self.counter = 1
        try:
            self.f = open(filename, mode)
            log = open('my_log.log', 'r')
            my_string = (log.readlines(-1)[-1]).split()[-2]
            print(f'counter is {my_string} you can see this and more debug info in log.fie')
            self.counter = int(my_string) + 1
        except:
            print('File not found or just created, you can see it on file_browser')

    def __enter__(self):
        self.loger.debug(f'{self.time}, Opened the {self.f}, open counter = {self.counter} times')
        return self.f

    def __exit__(self, *args):
        self.loger.debug(f'{self.time}, Closed the {self.f}, close counter = {self.counter} times')
        self.f.close()


with ConMan('test.txt', 'a') as f:
    f.write('append this some phrases\n')


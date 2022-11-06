import time
import random

class Timer:
    def __init__(self, exclude_timer_time = False, verbose = False, precision = 2):
        self.times = []
        self.verbose = verbose
        self.precision = precision

    def start(self):
        if len(self.times) != 0:
            print('Timer already started')
        else:
            self.times.append(time.time())
            if self.verbose == True:
                print('Timer Started')

    def lap(self):
        if len(self.times) == 0:
            print('Timer not yet started')
        else:
            self.times.append(time.time())
            if self.verbose == True:
                print(f'Lap Time:   {self.times[-1] - self.times[-2]:.{self.precision}f}')
                print(f'Total Time: {self.times[-1] - self.times[0]:.{self.precision}f}')

    def stop(self):
        if len(self.times) == 0:
            print('Timer not yet started')
        else:
            self.times.append(time.time())
            if self.verbose == True:
                if len(self.times) > 2:
                    print(f'Lap Time:   {self.times[-1] - self.times[-2]:.{self.precision}f}')
                print(f'Total Time: {self.times[-1] - self.times[0]:.{self.precision}f}')

    def report(self):
        if (len(self.times) == 0):
            print('Timer not yet started')
        else:
            for l in range(1,len(self.times)):
                print(f'Lap {l}:')
                print(f'\tLap Time:   {self.times[l] - self.times[l-1]:.{self.precision}f}')
                print(f'\tTotal Time: {self.times[l] - self.times[0]:.{self.precision}f}')


    def reset(self):
        self.times = []


if __name__ == '__main__':
    timer = Timer(verbose=True,precision=4)
    timer.start()
    for i in range(9):
        time.sleep(random.random()/10)
        timer.lap()
    time.sleep(random.random()/10)
    timer.stop()
    timer.report()
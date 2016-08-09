import time


class Timer(object):
    def __int__(self, verbose=False):
        self.verbose = verbose

    def __enter__(self):
        self._start__time = time.time()
        return  self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._end__time = time.time()
        self.secs = self._end__time - self._start__time
        self.millis = self.secs * 1000
        if self.verbose:
            print('elapasd time: {0:f} ms'.format(self.millis))
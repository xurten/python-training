# Tip 53 use threads for block operations
# GIL = Global Interpreter Lock, because GIT python does not allow to run parallel the byte code
# threads are useful for easy way of running many task, but one thread can be running only and later the next
# good for blocking operation in-out operations

import time
from threading import Thread


def factorize(number):
    for i in range(1, number + 1):
        if number % i == 0:
            yield i


numbers = [2139079, 1214759, 1516637, 1852285]


def example_without_thread():
    start = time.time()

    for number in numbers:
        list(factorize(number))

    end = time.time()
    delta = end - start
    print(f'Took {delta:.3f} s')


def example_with_thread():
    class FactorizeThread(Thread):
        def __init__(self, number):
            super().__init__()
            self.number = number

        def run(self):
            self.factors = list(factorize(self.number))

    start = time.time()
    threads = []
    for number in numbers:
        thread = FactorizeThread(number)
        thread.start()
        threads.append(thread)
    for thread in threads:
        thread.join()
    end = time.time()
    delta = end - start
    print(f'Took {delta:.3f} s')


example_without_thread()
example_with_thread()

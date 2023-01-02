# Tip 54 use lock for threads
from threading import Thread, Lock

HOW_MANY = 10 ** 5


class Counter:
    def __init__(self):
        self.count = 0

    def increment(self, offset):
        self.count += offset


def worker(index, counter):
    for _ in range(HOW_MANY):
        counter.increment(1)


def thread_example():
    how_many = 10 ** 5
    counter = Counter()
    threads = []
    for i in range(5):
        thread = Thread(target=worker, args=(i, counter))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    expected = how_many * 5
    found = counter.count
    print(f'found= {found}, expected = {expected}')


def thread_with_lock_example():
    class LockingCounter:
        def __init__(self):
            self.lock = Lock()
            self.count = 0

        def increment(self, offset):
            with self.lock:
                self.count += offset

    counter = LockingCounter()
    threads = []
    for i in range(5):
        thread = Thread(target=worker, args=(i, counter))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    expected = HOW_MANY * 5
    found = counter.count
    print(f'found= {found}, expected = {expected}')


thread_example()
thread_with_lock_example()

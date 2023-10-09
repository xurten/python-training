"""
Deadlocks: A deadlock occurs when two or more processes are unable to proceed
because each is waiting for the other to release a resource.

In this example, each process acquires one lock and then attempts to acquire the other.
If both processes acquire their first locks at roughly the same time, they can end up waiting
forever for the other to release its first lock - a classic deadlock.
"""

from multiprocessing import Process, Lock


def deadlock(lock1, lock2):
    with lock1:
        with lock2:
            print('This is a deadlock')


if __name__ == '__main__':
    lock1 = Lock()
    lock2 = Lock()

    Process(target=deadlock, args=(lock1, lock2)).start()
    Process(target=deadlock, args=(lock2, lock1)).start()
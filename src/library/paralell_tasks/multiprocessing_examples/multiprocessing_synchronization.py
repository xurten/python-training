from multiprocessing import Process, Lock
"""
Synchronization: Synchronization is used to control the access of multiple processes
to a shared resource. Here’s an example using a Lock
"""


def printer(item, lock):
    lock.acquire()
    try:
        print(item)
    finally:
        lock.release()


if __name__ == '__main__':
    lock = Lock()
    items = ['tango', 'foxtrot', 'lima']

    for item in items:
         Process(target=printer, args=(item, lock)).start()
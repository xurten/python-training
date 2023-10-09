from multiprocessing import Process, Value

"""
Race Conditions: A race condition occurs when two or more processes can access shared data
and they try to change it at the same time. As a result, the values of variables may be
unpredictable and vary depending on the timings of context switches of the processes.


In this example, process1 and process2 both increment the shared number by 100.
However, because they don’t use any synchronization mechanism like locks, the final value
of shared_number might not be 200 due to race conditions.
"""


def add_100(number):
    for _ in range(100):
        number.value += 1


if __name__ == '__main__':
    shared_number = Value('i', 0)
    process1 = Process(target=add_100, args=(shared_number,))
    process2 = Process(target=add_100, args=(shared_number,))

    process1.start()
    process2.start()

    process1.join()
    process2.join()

    print(shared_number.value)
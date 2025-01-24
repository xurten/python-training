import multiprocessing


class Counter:
    def __init__(self):
        self.value = multiprocessing.Value('i', 0)
        self.lock = multiprocessing.Lock()

    def increment(self):
        with self.lock:
            self.value.value += 1


def worker(counter, iterations):
    for _ in range(iterations):
        counter.increment()


def main():
    counter = Counter()
    num_processes = 5
    iterations_per_process = 1000

    processes = []

    for _ in range(num_processes):
        process = multiprocessing.Process(target=worker, args=(counter, iterations_per_process))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    print(f"Final Counter Value: {counter.value.value}")


if __name__ == '__main__':
    main()

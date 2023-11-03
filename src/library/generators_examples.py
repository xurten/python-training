
def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def simple_generator():
    yield 1
    yield 2
    yield 3


if __name__ == '__main__':
    fib_gen = fibonacci_generator()

    for i in range(10):
        print(next(fib_gen))

    generator = simple_generator()
    for i in range(3):
        print(next(generator))

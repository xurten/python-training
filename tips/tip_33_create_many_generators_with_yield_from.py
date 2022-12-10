# Tip 33 create many generators with yield

import timeit

N = 1000000


def child():
    for i in range(N):
        yield i


def slow():
    for i in child():
        yield i


def fast():
    yield from child()


baseline = timeit.timeit(stmt='for _ in slow():pass', globals=globals(), number=50)
print(f'Without yield from {baseline:.2f} s')
comparison = timeit.timeit(stmt='for _ in fast():pass', globals=globals(), number=50)
print(f'With yield from {comparison:.2f} s')

reduction = -(comparison-baseline) / baseline
print(f'{reduction:.1%} faster')


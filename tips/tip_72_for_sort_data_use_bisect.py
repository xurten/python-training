# Tip 72 for search in sorted data use bisect module
import timeit
from bisect import bisect_left
import random

iterations = 1000
size = 10 ** 5
data = list(range(size))
to_lookup = [random.randint(0, size) for _ in range(iterations)]


def example_for_search():
    index = data.index(91234)
    assert index == 91234

    index = bisect_left(data, 91234)
    assert index == 91234
    index = bisect_left(data, 91234.56)
    assert index == 91235


def run_linear(data, to_lookup):
    for index in to_lookup:
        data.index(index)


def run_bisect(data, to_lookup):
    for index in to_lookup:
        bisect_left(data, index)


def check_time_comparison():
    baseline = timeit.timeit(stmt='run_linear(data, to_lookup)', globals=globals(), number=10)
    print(f'Linear search time {baseline:.6f} s')
    comparison = timeit.timeit(stmt='run_bisect(data, to_lookup)', globals=globals(), number=10)
    print(f'Bisect search time {comparison:.6f} s')
    slowdown = 1 + ((baseline - comparison) / comparison)
    print(f'times less {slowdown:.1f} ')


if __name__ == '__main__':
    example_for_search()
    check_time_comparison()

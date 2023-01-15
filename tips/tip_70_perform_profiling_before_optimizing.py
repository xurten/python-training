# Tip 70 perform profiling before optimizing
# two python tools profile and cProfile(more extended in C language)
# modules : pstats, cProfile

# Columns of cProfile stats
# ncalls - number of function execution
# tottime - the number of seconds it took to execute the function,
# time for execution of other functions called by these functions
# is not taken into account
# percall - tottime / ncalls - average time of execution function
# cumtime - full time of execution of function
# percall - cumtime / percall - full average time of execution function
from bisect import bisect_left
from cProfile import Profile
from pstats import Stats
from random import randint


def insertion_sort(data, insert_function):
    result = []
    for value in data:
        insert_function(result, value)
    return value


def insert_value(array, value):
    for i, existing in enumerate(array):
        if existing > value:
            array.insert(i, value)
            return
    array.append(value)


def better_insert_value(array, value):
    i = bisect_left(array, value)
    array.insert(i, value)


def get_data(insert_function):
    max_size = 10 ** 4
    data = [randint(0, max_size) for _ in range(max_size)]
    test = lambda: insertion_sort(data, insert_function)
    return test


def run_profiler(test):
    profiler = Profile()
    profiler.runcall(test)

    stats = Stats(profiler)
    stats.strip_dirs()
    stats.sort_stats('cumulative')
    stats.print_stats()
    stats.print_callers()


run_profiler(get_data(insert_value))
run_profiler(get_data(better_insert_value))
# Tip 81 use module tracemalloc for memory leaks

import os
import gc
import tracemalloc


class MyObject:
    def __init__(self):
        self.data = os.urandom(100)


def get_data():
    values = []
    for _ in range(100):
        obj = MyObject()
        values.append(obj)
    return values


def run():
    deep_values = []
    for _ in range(100):
        deep_values.append(get_data())
    return deep_values


def get_object_status_before():
    found_objects = gc.get_objects()
    print(f'Number of objects before: {len(found_objects)}')


def get_object_status_after():
    found_objects = gc.get_objects()
    print(f'Number of objects after: {len(found_objects)}')
    for obj in found_objects[:3]:
        print(repr(obj)[:100])


def check_with_trace_malloc():
    tracemalloc.start(10)
    first_time = tracemalloc.take_snapshot()
    reference = run()
    second_time = tracemalloc.take_snapshot()
    stats = second_time.compare_to(first_time, 'lineno')
    for stat in stats[:3]:
        print(stat)
    return reference


get_object_status_before()
reference = check_with_trace_malloc()
# reference = run()
get_object_status_after()

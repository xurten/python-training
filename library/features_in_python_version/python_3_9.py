# whats new in python3 all in all https://python-future.org/compatible_idioms.html
# https://www.linkedin.com/learning/first-look-python-3-9/
import logging
import functools
import time

logger = logging.getLogger(__name__)


def merge_two_dictionaries():
    first_dictionary = {1: 'aaaa'}
    second_dictionary = {2: 'bbbb'}
    first_dictionary.update(second_dictionary)
    logger.error(f'Merge of two dictionaries: {first_dictionary}')


def new_string_methods():
    # new string methods removesuffix, removeprefix
    file_name = "bbbaaaa.jpg".removesuffix('.jpg')
    print(file_name)
    file_name = file_name.removeprefix('bbb')
    print(file_name)


def new_zoneinfo_module():
    # new module for zoneinfo
    from datetime import datetime
    import zoneinfo
    new_date = datetime(2022, 8, 2, 12, tzinfo=zoneinfo.ZoneInfo("America/Los_Angeles"))
    print(new_date)
    print(new_date.tzinfo)


# Expensive function
@functools.lru_cache(maxsize=None)
def expensive_computation(x):
    time.sleep(2)  # Simulate a time-consuming computation
    return x * x


def test_expensive_computation():
    start_time = time.time()
    first_result = expensive_computation(4)
    duration_first_call = time.time() - start_time

    start_time = time.time()
    second_result = expensive_computation(4)
    duration_second_call = time.time() - start_time

    assert first_result == 16
    assert second_result == 16

    duration_first_call = round(duration_first_call, 7)
    duration_second_call = round(duration_second_call, 7)

    assert duration_first_call > 1  # Ensure the first call takes time
    assert duration_second_call < 1  # Ensure the second call is fast due to caching
    logger.error(f"First call duration: {duration_first_call:.6f} s")
    logger.error(f"Second call duration: {duration_second_call:.6f} s")


class ExampleClass:

    @functools.cached_property
    def expensive_property(self):
        time.sleep(2)  # Simulate a time-consuming computation
        return "Expensive Result"


def test_cached_property():
    example_instance = ExampleClass()
    start_time = time.time()
    result1 = example_instance.expensive_property
    duration_first_call = time.time() - start_time

    start_time = time.time()
    result2 = example_instance.expensive_property
    duration_second_call = time.time() - start_time

    assert result1 == "Expensive Result"
    assert result2 == "Expensive Result"

    assert duration_first_call > 1  # Ensure the first call takes time
    assert duration_second_call < 1  # Ensure the second call is fast due to caching
    logger.error(f"First call duration: {duration_first_call:.6f} s")
    logger.error(f"Second call duration: {duration_second_call:.6f} s")


if __name__ == '__main__':
    merge_two_dictionaries()
    new_string_methods()
    new_zoneinfo_module()
    test_expensive_computation()
    test_cached_property()
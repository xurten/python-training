# Tip 31 Keep defensive position when operating through arguments
# __iter__(), iter(), next(), collections.abc.Iterator
from collections.abc import Iterator


def normalize(numbers):
    total = sum(numbers)
    result = []
    for value in numbers:
        percent = 100 * value / total
        result.append(percent)
    return result


visits = [15, 35, 80]
percentages = normalize(visits)
print(percentages)


class ReadVisits:
    def __init__(self, data_path):
        self.data_path = data_path

    def __iter__(self):
        with open(self.data_path) as f:
            for line in f:
                yield int(line)


visits = ReadVisits('../test_data/tip_31_visits')
percentages = normalize(visits)
print(percentages)
assert sum(percentages) == 100.0


def normalize_defensive(numbers):
    if iter(numbers) is iter(numbers):
        raise TypeError('Need container')
    total = sum(numbers)
    result = []
    for value in numbers:
        percent = 100 * value / total
        result.append(percent)
    return result


visits = ReadVisits('../test_data/tip_31_visits')
percentages = normalize_defensive(visits)
print(percentages)


def normalize_defensive_second(numbers):
    if isinstance(numbers, Iterator):
        raise TypeError('Need container')
    total = sum(numbers)
    result = []
    for value in numbers:
        percent = 100 * value / total
        result.append(percent)
    return result


visits = [15, 35, 80]
percentages = normalize_defensive_second(visits)
print(percentages)

visits = [15, 35, 80]
it = iter(visits)
try:
    normalize_defensive_second(it)
except TypeError:
    print('TypeError: Need container')

# Tip 38 For simpple interface accept functions than classes
# __call__ allows execute clases instances as functions
from collections import defaultdict

current = {'green': 12, 'blue': 3}
increments = [
    ('red', 10),
    ('blue', 17),
    ('orange', 5)
]


def without_class():
    def increment_with_report(current, increments):
        added_count = 0

        def missing():
            nonlocal added_count
            added_count += 1
            return 0

        result = defaultdict(missing, current)
        for key, amount in increments:
            result[key] += amount
        return result, added_count

    result, count = increment_with_report(current, increments)
    print(f'{result} {count}')
    assert count == 2


def with_class():
    class CountMissing:
        def __init__(self):
            self.added = 0

        def missing(self):
            self.added += 1
            return 0

    counter = CountMissing()
    result = defaultdict(counter.missing, current)
    for key, amount in increments:
        result[key] += amount
    assert counter.added == 2


def with_class_and_call_method():
    class CountMissing:
        def __init__(self):
            self.added = 0

        def __call__(self):
            self.added += 1
            return 0

    counter = CountMissing()
    assert counter() == 0
    assert callable(counter)
    result = defaultdict(counter, current)
    for key, amount in increments:
        result[key] += amount
    assert counter.added == 2


without_class()
with_class()
with_class_and_call_method()

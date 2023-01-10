# Tip 43 use inheritance after collections.abc
import collections
# Documentation: https://docs.python.org/3/library/collections.abc.html
from collections.abc import Sequence, Sized


class Frequency(list):
    def __init__(self, members):
        super().__init__(members)

    def frequency(self):
        counts = {}
        for item in self:
            counts[item] = counts.get(item, 0) + 1
        return counts


foo = Frequency(['a', 'b', 'a', 'c', 'b', 'a', 'd'])
print(repr(foo))
foo.pop()
print(repr(foo))
print(foo.frequency())


# bar = [1,2,3], bar[0] == bar.__getitem__(0)
class C(Sized):
    pass

    def __len__(self):
        return 5


a = C()
print(a.__dict__)

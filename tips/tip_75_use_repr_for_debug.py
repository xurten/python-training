# Tip 75 use repr for debug
# Both __str__ and __repr__ functions return string representation of the object
# __str__ string representation is more human-friendly and for logging
# __repr__ information about object so that it can be rebuilt again
# !r - convert the value with repr()
# !s - convert the value with str()
import datetime

now = datetime.datetime.now()
print(now.__str__())
print(now.__repr__())


class BetterClass:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'BetterClass({self.x!r}, {self.y!r})'


obj = BetterClass(1, 'bar')
print(obj)
print(obj.__dict__)

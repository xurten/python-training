# Tip 17 use defaultdict instead of setdefault()

from collections import defaultdict


class Visits:
    def __init__(self):
        self.data = defaultdict(set)

    def add(self, country, city):
        self.data[country].add(city)


visits = Visits()
visits.add('UK', 'Bath')
visits.add('UK', 'London')

print(visits.data)


def def_value():
    return "Not Present"


def return_default_value():
    return "Default value"


d = defaultdict(return_default_value)
d['a'] = 1
d['b'] = 2

print(d['a'])
print(d['b'])
print(d['c'])

# bad example

dictionary = {}
value = dictionary.setdefault('new', 'if the key not exists')
print(value)

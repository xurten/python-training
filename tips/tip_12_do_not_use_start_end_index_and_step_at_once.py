# Tip 12 do not use start end index and step at once,
# better use islice or use step > 0
from itertools import islice


def example():
    a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    print(f'a[::2] = {a[::2]}')
    print(f'a[::-2] = {a[::-2]}')
    print(f'a[2::2] = {a[2::2]}')
    print(f'a[-2::-2] = {a[-2::-2]}')
    print(f'a[-2:2:-2] = {a[-2:2:-2]}')
    print(f'a[2:2:-2] = {a[2:2:-2]}')
    print(list(islice(a, 1, 5, 2)))


example()

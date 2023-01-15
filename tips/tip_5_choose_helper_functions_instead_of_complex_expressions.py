# Tip 5 choose helper functions instead of complex expressions
# method get if not key then return the second parameter
from urllib.parse import parse_qs

my_values = parse_qs('red=5&blue=0&green=', keep_blank_values=True)


def long_version():
    print(my_values)
    red = int(my_values.get('red', [''])[0] or 0)
    green = int(my_values.get('green', [''])[0] or 0)
    opacity = int(my_values.get('opacity', [''])[0] or 0)

    print(f' red {red!r} green {green!r} opacity {opacity!r}')


def get_first_int(values, key, default=0):
    found = values.get(key, [''])
    if found[0]:
        return int(found[0])
    return default


def short_version():
    red = get_first_int(my_values, 'red')
    green = get_first_int(my_values, 'green')
    opacity = get_first_int(my_values, 'opacity')

    print(f' red {red!r} green {green!r} opacity {opacity!r}')


if __name__ == '__main__':
    long_version()
    short_version()

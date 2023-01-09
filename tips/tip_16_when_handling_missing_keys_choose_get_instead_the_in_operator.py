# Tip 16 when handling missing keys, choose get instead of the in operator

votes = {
    'first': ['bartek', 'alicja'],
    'second': ['celina', 'dorota']
}
key = 'foo'
key_second = 'foo2'


def example_with_in():
    if key in votes:
        names = votes[key]
    else:
        votes[key] = names = []
    print(votes)


def example_with_get():
    if (names := votes.get(key_second)) is None:
        votes[key_second] = names = []
    print(votes)


def example_with_setdefault():
    data = {}
    value = []
    data.setdefault(key, value)
    print(data)
    value.append('hi')
    print(data)


example_with_in()
example_with_get()
example_with_setdefault()

# Tip 36 use module itertools for iterators


# chain()
from itertools import chain, repeat, zip_longest, islice, takewhile, filterfalse, permutations, combinations

it = chain([1, 2, 3], [2, 3, 4])
print(list(it))

# repeat()
it = repeat('world', 100)
print(list(it))

# method cycle()
it = repeat([1, 2])
result = [next(it) for _ in range(10)]
print(result)

# zip longest()
key = ['first', 'second', 'third']
values = [1, 2]

normal = list(zip(key, values))
print(f'zip: {normal}')

it = zip_longest(key, values, fillvalue='empty')
longest = list(it)
print(f'zip_longest: {longest}')

# islice()
values = [_ for _ in range(11)]
print(values)
first_five = islice(values, 5)
middle_odds = islice(values, 2, 8, 2)
print(f'{list(first_five)} {list(middle_odds)}')

# takewhile()
values = [_ for _ in range(11)]
print(list(takewhile(lambda x: x < 7, values)))

# filterfalse()
values = [_ for _ in range(11)]
even = lambda x: x % 2 == 0
print(f'{list(filterfalse(even, values))}')

# permutations()
it = permutations([1, 2, 3, 4], 2)
print(list(it))

# combinations()
it = combinations([1, 2, 3, 4], 2)
print(list(it))

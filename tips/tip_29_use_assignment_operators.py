# Tip 29 use assignment operators(walrus operator)

stock = {
    'pencil': 123,
    'paper': 35,
    'phone': 8,
    'laptop': 24
}

order = ['paper', 'phone', 'water']


def get_batches(count, size):
    return count // size


found = ((name, batches) for name in order
         if (batches := get_batches(stock.get(name, 0), 8)))

print(next(found))
print(next(found))

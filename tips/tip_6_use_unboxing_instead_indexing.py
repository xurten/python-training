# Tip 6 use unboxing instead of indexing

snacks = [('pizza', 350), ('ice cream', 240), ('chips', 100), ('apple', 50)]


# normal way
def bad_iteration():
    for i in range(len(snacks)):
        item = snacks[i]
        name = item[0]
        calories = item[1]
        print(f'{i + 1}: {name} has {calories} calories')


def good_iteration():
    for rank, (name, calories) in enumerate(snacks, 1):
        print(f'{rank}: {name} has {calories} calories')


bad_iteration()
good_iteration()

# Tip 11 Skillfully divide the sequences

# [start_index, end_index, where start_index is included in collection and end_index no
def example_1():
    a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    print(a)
    print(f'a[:] = {a[:]}')
    print(f'a[:5] = {a[:5]}')
    print(f'a[:-1] = {a[:-1]}')
    print(f'a[4:] = {a[4:]}')
    print(f'a[-3:] = {a[-3:]}')
    print(f'a[2:5] = {a[2:5]}')
    print(f'a[2:-1] = {a[2:-1]}')
    print(f'a[-3:-1] = {a[-3:-1]}')
    # create copy if there is no start_index and no end_index
    b = a[:]
    a == b and b is not a


example_1()
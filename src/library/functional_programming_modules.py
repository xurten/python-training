from itertools import count, cycle, dropwhile, filterfalse, permutations, repeat
from more_itertools.more import repeat_each

# itertools
# make an iterator
# https://pypi.org/project/more-itertools/
def count_example():
    c = count(10)
    for i in range(1, 10):
        print(c.__next__())


def cycle_example():
    c = cycle('ABCDE')
    for i in range(1, 20):
        print(c.__next__())


def dropwhile_example():
    even_list = dropwhile(lambda x: x < 5, [1, 2, 3, 4, 5, 6, 7, 8])
    for i in range(1, 5):
        print(even_list.__next__())


def filter_false_example():
    list = filterfalse(lambda x: x % 2, range(10))
    for i in range(1, 5):
        print(list.__next__())


def permutations_example():
    list_of_permutation = permutations('ABCD', 2)
    for i in range(1, 20):
        try:
            print(list_of_permutation.__next__())
        except:
            print('Out of next iteration')


def list_example():
    new_map = list(map(pow, range(10), repeat(2)))
    print(new_map)


def repeat_example():
    each_list = list(repeat_each('ABC', 3))
    print(each_list)


if __name__ == '__main__':
    # count_example()
    # cycle_example()
    # dropwhile_example()
    # filter_false_example()
    # permutations_example()
    #list_example()

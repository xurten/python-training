# Tip 32 use generators for big comprehension lists(generator expressions)
# comprehension lists use a lot of memory for big lists
# generator expression can lead to small memory usage
# connection of generator expression and comprehension lists can be very efficient and very fast for memory usage

MAX_NUMBER = 20
list_iterator = (x for x in range(MAX_NUMBER))

roots = ((x, x ** 2) for x in list_iterator)
numbers = [next(roots) for x in range(MAX_NUMBER)]
print(numbers)

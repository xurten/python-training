# Tip 22 use star argument
# if last argument has * it can be optional, several arguments
# use * with generator can leads to high memory usage


def log(message, *values):
    if not values:
        print(message)
    else:
        values_str = ', '.join((str(x) for x in values))
        print(f'{message}: {values_str}')


log('My numbers', 1, 2)
log('hello')


#Not recommended use * with generator
def my_generator():
    for i in range(10):
        yield i


def my_func(*args):
    print(args)


it = my_generator()
my_func(*it)

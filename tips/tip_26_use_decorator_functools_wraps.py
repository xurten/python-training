# Tip Use decorator functools wraps
# functools.wraps It updates the wrapper function
# to look like wrapped function by copying attributes
# such as __name__, __doc__ (the docstring), etc.
from functools import wraps


def trace(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f'{func.__name__} ({args!r}, {kwargs!r}) -> {result!r}')
        return result

    return wrapper


@trace
def fibonacci(n):
    """Value of n-th fibonacii"""
    if n in (0, 1):
        return n
    return fibonacci(n - 2) + fibonacci(n - 1)


def trace_second(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f'{func.__name__} ({args!r}, {kwargs!r}) -> {result!r}')
        return result
    return wrapper


@trace_second
def fibonacci_second(n):
    """Value of n-th fibonacii"""
    if n in (0, 1):
        return n
    return fibonacci_second(n - 2) + fibonacci_second(n - 1)


fibonacci(5)
help(fibonacci)
fibonacci_second(6)
help(fibonacci_second)

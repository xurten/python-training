# Tip 66 use contextlib for multi try-finally
# # command with allows multi-usage of block try-finally and less code
# https://docs.python.org/3/library/contextlib.html

import logging
from contextlib import contextmanager


def my_function():
    logging.debug('Debug information')
    logging.error('Error information')
    logging.debug('More debug information')


@contextmanager
def debug_loggin(level):
    logger = logging.getLogger()
    old_level = logger.getEffectiveLevel()
    logger.setLevel(level)
    try:
        yield
    finally:
        logger.setLevel(old_level)


with debug_loggin(logging.ERROR):
    print('Inside:')
    my_function()
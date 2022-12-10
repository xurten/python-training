# Tip 24 Use None and doccstring for dynamic default arguments
from datetime import datetime
from time import sleep
from typing import Optional


def bad_log(message, when=datetime.now()):
    print(f'{when}: {message}')


bad_log('hellow version 1.0')
sleep(0.1)
bad_log('hellow again version 1.0')


def better_log(message, when=None):
    """Display debug information

    :param message: Message for display
    :param when: default date
    """
    if when is None:
        when = datetime.now()
    print(f'{when}: {message}')


better_log('hellow version 1.1')
sleep(0.1)
better_log('hellow again version 1.1')


def better_log_with_optional(message: str, when: Optional[datetime] = None) -> None:
    """Display debug information

    :param message: Message for display
    :param when: default date
    """
    if when is None:
        when = datetime.now()
    print(f'{when}: {message}')


better_log_with_optional('hellow version 1.2')
sleep(0.1)
better_log_with_optional('hellow again version 1.2')
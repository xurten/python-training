import logging
from datetime import date

logger = logging.getLogger(__name__)


def the_walrus_operator():
    a = range(1, 20)
    if (n := len(a)) > 10:
        logger.error(f"List is too long ({n} elements, expected <= 10)")


def positional_only_parameters():
    def f(a, b, /, c, d, *, e, f):
        logger.error(f"{a=}, {b=}, {c=}, {d=}, {e=}, {f=}")

    f(10, 20, 30, d=40, e=50, f=60)
    try:
        f(10, b=20, c=30, d=40, e=50, f=60)
    except Exception as ex:
        logger.error(ex)
    try:
        f(10, 20, 30, 40, 50, f=60)
    except Exception as ex:
        logger.error(ex)


def f_strings_self_documenting():
    user = 'eric_idle'
    member_since = date(1975, 7, 31)
    logger.error(f'{user=} {member_since=}')
    delta = date.today() - member_since
    logger.error(f'{user=!s} {delta.days=:,d}')


if __name__ == '__main__':
    the_walrus_operator()
    positional_only_parameters()
    f_strings_self_documenting()

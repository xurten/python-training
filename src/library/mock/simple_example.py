import datetime
from unittest import TestCase
from unittest.mock import Mock

from _pytest import unittest

tuesday = datetime.datetime(year=2019, month=1, day=1)
saturday = datetime.datetime(year=2019, month=1, day=5)
tmp = datetime.datetime.today()
datetime_mock = Mock()


def is_weekday():
    today = datetime_mock.datetime.today()
    print(today)
    return 0 <= today.weekday() < 5


class TestCalendar(TestCase):
    def test_tuesday(self):
        datetime_mock.datetime.today.return_value = tuesday
        assert is_weekday()

    def test_saturday(self):
        datetime_mock.datetime.today.return_value = saturday
        assert not is_weekday()


if __name__ == '__main__':
    unittest.main()

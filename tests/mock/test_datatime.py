import unittest
from unittest import TestCase

from library.mock import tuesday, saturday, is_weekday, datetime_mock


class TestCalendar(TestCase):
    def test_tuesday(self):
        datetime_mock.datetime.today.return_value = tuesday
        assert is_weekday()

    def test_saturday(self):
        datetime_mock.datetime.today.return_value = saturday
        assert not is_weekday()


if __name__ == '__main__':
    unittest.main()

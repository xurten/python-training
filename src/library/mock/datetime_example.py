import datetime
from unittest.mock import Mock

tuesday = datetime.datetime(year=2019, month=1, day=1)
saturday = datetime.datetime(year=2019, month=1, day=5)
tmp = datetime.datetime.today()
datetime_mock = Mock()


def is_weekday():
    today = datetime_mock.datetime.today()
    print(today)
    return 0 <= today.weekday() < 5


if __name__ == '__main__':
    print(is_weekday())

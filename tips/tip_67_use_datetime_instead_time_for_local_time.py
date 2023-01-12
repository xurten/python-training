# Tip 67 use datetime instead of time
# module time is connected with platform
# use time only for conversion between local time and UTC
import time
from datetime import datetime, timezone
import pytz

TIME_FORMAT = '%Y-%m-%d %H:%M:%S'


def example_with_time():
    now = 1552774475
    local_tuple = time.localtime(now)

    print(time_str := time.strftime(TIME_FORMAT, local_tuple))

    time_tuple = time.strptime(time_str, TIME_FORMAT)
    utc_now = time.mktime(time_tuple)
    print(utc_now)


def example_with_datetime():
    now = datetime(2019, 3, 16, 22, 14, 35)
    now_utc = now.replace(tzinfo=timezone.utc)
    now_local = now_utc.astimezone()
    print(now_local)
    time_str = '2019-03-16 15:14:35'
    now = datetime.strptime(time_str, TIME_FORMAT)
    time_tuple = now.timetuple()
    utc_now = time.mktime(time_tuple)
    print(utc_now)


def example_with_pytz():
    arrival_nyc = '2019-03-16 23:33:35'
    nyc_dt_naive = datetime.strptime(arrival_nyc, TIME_FORMAT)
    eastern = pytz.timezone('US/Eastern')
    nyc_dt = eastern.localize(nyc_dt_naive)
    utc_dt = pytz.utc.normalize(nyc_dt.astimezone(pytz.utc))
    print(utc_dt)


example_with_time()
example_with_datetime()
example_with_pytz()

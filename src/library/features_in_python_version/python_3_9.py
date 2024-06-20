# whats new in python3 all in all https://python-future.org/compatible_idioms.html
# https://www.linkedin.com/learning/first-look-python-3-9/
import logging

logger = logging.getLogger(__name__)


def merge_two_dictionaries():
    first_dictionary = {1: 'aaaa'}
    second_dictionary = {2: 'bbbb'}
    first_dictionary.update(second_dictionary)
    logger.error(f'Merge of two dictionaries: {first_dictionary}')


def new_string_methods():
    # new string methods removesuffix, removeprefix
    file_name = "bbbaaaa.jpg".removesuffix('.jpg')
    print(file_name)
    file_name = file_name.removeprefix('bbb')
    print(file_name)


def new_zoneinfo_module():
    # new module for zoneinfo
    from datetime import datetime
    import zoneinfo
    new_date = datetime(2022, 8, 2, 12, tzinfo=zoneinfo.ZoneInfo("America/Los_Angeles"))
    print(new_date)
    print(new_date.tzinfo)


if __name__ == '__main__':
    merge_two_dictionaries()
    new_string_methods()
    new_zoneinfo_module()

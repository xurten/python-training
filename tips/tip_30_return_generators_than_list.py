# Tip 30 Think about to use generators than return a list
import itertools
import os
import string
from random import Random

STRING_LENGTH = 1000000
FILE_NAME = 'file.txt'

def index_words(text):
    result = []
    if text:
        result.append(0)
    for index, letter in enumerate(text):
        if letter == ' ':
            result.append(index + 1)
    return result


def get_random_string(length):
    tmp_random = Random()
    return ''.join(tmp_random.choice(string.printable) for i in range(length))


def create_file_with_content(content):
    if os.path.isfile(FILE_NAME):
        raise FileExistsError
    with open(FILE_NAME, 'w', encoding='utf-8') as f:
        f.writelines(content)


large_string = get_random_string(STRING_LENGTH)
print(index_words(large_string))
create_file_with_content(large_string)


def index_words_iter(text):
    if text:
        yield 0
    for index, letter in enumerate(text):
        if letter == ' ':
            yield index + 1


print(list(index_words_iter(large_string)))


def index_file_iter(handle):
    offset = 0
    for line in handle:
        if line:
            yield offset
        for letter in line:
            offset += 1
            if letter == ' ':
                yield offset


def open_with_iter():
    with open(FILE_NAME, 'r') as f:
        it = index_file_iter(f)
        result = itertools.islice(it, 0, 10)
        print(list(result))
    os.remove(FILE_NAME)


open_with_iter()

import re
import array as arr

# Comprehension List
x = [i for i in range(10)]
# print(x)
# Comprehension Dictionary
y = {i: i + 2 for i in range(4)}
# print(y)
# Slicing [start:end:step]
# print(x[0:5:1])
# Lambda function
# sum = lambda x, y: x + y
# print(sum(1000,2000))
# Reverse copy of array and list
my_array = arr.array('i', [1, 2, 3, 4, 5])


# print(my_array[::-1])
# print([i for i in range(20)][::-1])


def use_enumerate_example():
    new_list = [1, 5, 3, 5]
    for i in enumerate(new_list):
        print(f"{i} {i[0]} {i[1]}")


def get_yield():
    yield 1
    yield 2
    yield 3


def use_yield_example():
    tmp = get_yield()
    print(tmp.__next__())
    print(tmp.__next__())
    print(tmp.__next__())


def cube(y):
    return y * y * y


if __name__ == '__main__':
    use_enumerate_example()
    use_yield_example()
    a = 6564424525
    b = 323252462
    print(a % b)
    print(a / b)
    print('aaa')
    new_str = ''
    elements = list(range(1, 10))
    print(type(elements))
    # new_list = ["{s}".format(x) for x in elements]
    # new_str = ''.join(new_list)
    print(new_str)

    def replace_logic_operators(line):
        and_count = line.count(" && ")
        result = line
        while and_count > 0:
            result = result.replace(" && ", " and ", and_count)
            and_count = result.count(" && ")

        or_count = result.count(" || ")
        while or_count > 0:
            result = result.replace(" || ", " or ", or_count)
            or_count = result.count(" || ")
        return result


print("regex")
regex_pattern = r"(.)"  # Do not delete 'r'.
print(str(bool(re.match(regex_pattern, "^M{0,4}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$"))))

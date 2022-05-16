# Comprehension List
x = [i for i in range(10)]
# print(x)
# Comprehension Dictionary
y = {i: i + 2 for i in range(4)}
# print(y)
# Slicing [start:end:step]
# print(x[0:5:1])
# Lambda function
sum = lambda x, y: x + y
# print(sum(1000,2000))
# Reverse copy of array and list
import array as arr

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


def lambda_example():
    g = lambda x: x * x * x
    print(g(5))


if __name__ == '__main__':
    use_enumerate_example()
    use_yield_example()
    lambda_example()

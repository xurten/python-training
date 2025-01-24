# Random order of elements
from random import shuffle


def get_random_order_of_list(random_list):
    shuffle(random_list)
    print(random_list)
    return random_list


if __name__ == '__main__':
    x = ['Keep', 'The', 'Blue', 'Flag', 'Flying', 'High']
    get_random_order_of_list(x)
    number_list = [i for i in range(10)]
    get_random_order_of_list(number_list)

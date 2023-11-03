if __name__ == '__main__':
    my_dict = {'a': 3, 'b': 1, 'c': 2}
    sorted_dict = sorted(my_dict.items(), key=lambda x: x[1])
    print(sorted_dict)
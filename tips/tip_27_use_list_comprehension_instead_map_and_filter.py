# Tip 27 use list comprehension instead of map() and filter()

# examples for list
numbers = [1, 2, 3, 4, 5, 6, 7]

squares = [x ** 2 for x in numbers]
print(squares)
even_squares = [x ** 2 for x in numbers if x % 2 == 0]
print(even_squares)
# with map and filter
alt = map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, numbers))
print(list(alt))

# examples for dictionary
even_squares_dict = {x: x ** 2 for x in numbers if x % 2 == 0}
threes_cubed_set = {x ** 3 for x in numbers if x % 3 == 0}
print(even_squares_dict)
print(threes_cubed_set)

# with map and filter
alt_dict = dict(map(lambda x: (x, x ** 2), filter(lambda x: x % 2 == 0, numbers)))
alt_set = set(map(lambda x: x ** 3, filter(lambda x: x % 3 == 0, numbers)))
print(alt_dict)
print(alt_set)

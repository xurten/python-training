# Tip 21 Closures with the scope of the variable

def sort_priority(values, group):
    def helper(x):
        if x in group:
            return (0, x)
        return (1, x)

    values.sort(key=helper)


numbers = [8, 1, 4, 2, 4, 1, 8, 9, 5]
group = {2, 3, 5, 7}
sort_priority(numbers, group)
print(numbers)


def sort_priority3(numbers, group):
    found = False

    def helper(x):
        nonlocal found
        if x in group:
            found = True
            return (0, x)
        return (1, x)

    numbers.sort(key=helper)


numbers = [8, 1, 4, 2, 4, 1, 8, 9, 5]
group = {2, 3, 5, 7}
sort_priority3(numbers, group)
print(numbers)


class Sorter:
    def __init__(self, group):
        self.group = group
        self.found = False

    def __call__(self, x):
        if x in self.group:
            self.found = True
            return (0, x)
        return (1, x)


numbers = [8, 1, 4, 2, 4, 1, 8, 9, 5]
group = {2, 3, 5, 7}
sorter = Sorter(group)
numbers.sort(key=sorter)
print(numbers)

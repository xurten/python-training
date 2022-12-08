# Tip 13 Use catch all instead of indexes

people_ages = [10, 30, 50, 12, 80, 67, 40, 35, 26]


def bad_approach():
    people_ages_sorted = sorted(people_ages, reverse=True)
    oldest, second_oldest = people_ages_sorted[0], people_ages_sorted[1]
    print(oldest, second_oldest)


def better_approach():
    people_ages_sorted = sorted(people_ages, reverse=True)
    oldest, second_oldest, *others = people_ages_sorted
    print(oldest, second_oldest, others)


bad_approach()
better_approach()
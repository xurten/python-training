from collections import namedtuple


def get_person_info():
    name = "John Doe"
    age = 30
    country = "USA"
    return name, age, country


def get_city_information():
    location = (40.7128, -74.0060)  # New York City coordinates
    city_info = {location: 'New York City'}
    return city_info


if __name__ == '__main__':
    person_info = get_person_info()
    print(person_info)
    # unpack values
    name, age, country = person_info
    print(name)  # Output: John Doe
    # dictionary keys(immutable)
    print(get_city_information())
    # database record
    user_record = ('John Doe', 'johndoe@email.com', 30)
    print(user_record)
    # named tuples
    Point = namedtuple('Point', ['x', 'y'])
    p = Point(1, 2)
    print(p.x, p.y)

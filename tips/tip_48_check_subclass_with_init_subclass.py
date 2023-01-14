# Tip 48 check subclass with __init_subclass__
# Always use self for the first argument to instance methods
# Always use cls for the first argument to class methods


def example_with_new():
    class Meta(type):
        def __new__(meta, name, bases, class_dict):
            print(f'{meta}.__new__() for {name}')
            print(f'Bases {bases}')
            print(class_dict)
            return type.__new__(meta, name, bases, class_dict)

    class MyClass(metaclass=Meta):
        stuff = 123

        def foo(self):
            pass

    class MySubclass(MyClass):
        other = 567

        def bar(self):
            pass


def example_with_polygon():
    class ValidatePolygon(type):
        def __new__(meta, name, bases, class_dict):
            if bases:
                if class_dict['sides'] < 3:
                    raise ValueError('Must have at least 3 sides')
            return type.__new__(meta, name, bases, class_dict)

    class Polygon(metaclass=ValidatePolygon):
        sides = None

        @classmethod
        def interior_angles(cls):
            return (cls.sides - 2) * 180

    class Triangle(Polygon):
        sides = 3

    class Rectangle(Polygon):
        sides = 4

    class Nonagon(Polygon):
        sides = 9

    class Line(Polygon):
        sides = 2

    assert Triangle.interior_angles() == 180
    assert Rectangle.interior_angles() == 360
    assert Nonagon.interior_angles() == 1260


def better_example_with_polygon():
    class BetterPolygon:
        sides = None

        def __init_subclass__(cls):
            super().__init_subclass__()
            if cls.sides < 3:
                raise ValueError('Must have at least 3 sides')

        @classmethod
        def interior_angles(cls):
            print(cls.__dict__)
            return (cls.sides - 2) * 180

    class Hexagon(BetterPolygon):
        sides = 6

    assert Hexagon.interior_angles() == 720


def example_with_two_metadata_classes():
    class Filled:
        color = None

        def __init_subclass__(cls):
            super().__init_subclass__()
            if cls.color not in ('red', 'green', 'blue'):
                raise ValueError('Need correct color')

    class Polygon:
        sides = None

        def __init_subclass__(cls):
            super().__init_subclass__()
            if cls.sides < 3:
                raise ValueError('Must have at least 3 sides')

        @classmethod
        def interior_angles(cls):
            print(cls.__dict__)
            return (cls.sides - 2) * 180

    class RedTriangle(Filled, Polygon):
        color = 'red'
        sides = 3

    ruddy = RedTriangle()
    assert isinstance(ruddy, Filled)
    assert isinstance(ruddy, Polygon)

    class BlueLine(Filled, Polygon):
        color = 'blue'
        sides = 2


def example_with_diamond_hierarchy():
    class Top:
        def __init_subclass__(cls):
            super().__init_subclass__()
            print(f'Top for {cls}')

    class Left(Top):
        def __init_subclass__(cls):
            super().__init_subclass__()
            print(f'Left for {cls}')

    class Right(Top):
        def __init_subclass__(cls):
            super().__init_subclass__()
            print(f'Right for {cls}')

    class Bottom(Left, Right):
        def __init_subclass__(cls):
            super().__init_subclass__()
            print(f'Bottom for {cls}')


# example_with_new()
# example_with_polygon()
# better_example_with_polygon()
# example_with_two_metadata_classes()
example_with_diamond_hierarchy()

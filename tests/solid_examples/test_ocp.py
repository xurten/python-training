import pytest

from library.solid_examples.ocp import Shape, Rectangle, Circle


class TestShape:

    #  Call the area() method on an instance of Shape and expect no errors
    def test_area_no_errors(self):
        shape = Shape()
        try:
            shape.area()
        except Exception as e:
            pytest.fail(f"Unexpected error: {e}")

    #  Call the area() method on an instance of Rectangle and expect the correct area to be returned
    def test_rectangle_area(self):
        rectangle = Rectangle(4, 5)
        assert rectangle.area() == 20

    #  Call the area() method on an instance of Circle and expect the correct area to be returned
    def test_circle_area(self):
        circle = Circle(3)
        assert circle.area() == 28.26

    #  Call the area() method on an instance of Rectangle with width or height equal to 0 and expect 0 to be returned
    def test_rectangle_zero_area(self):
        rectangle = Rectangle(0, 5)
        assert rectangle.area() == 0

    #  Call the area() method on an instance of Circle with radius equal to 0 and expect 0 to be returned
    def test_circle_zero_area(self):
        circle = Circle(0)
        assert circle.area() == 0

    #  Call the area() method on an instance of Circle with a very large radius and expect a correct area to be returned
    def test_circle_large_radius_area(self):
        circle = Circle(1000000)
        assert circle.area() == 3140000000000.0


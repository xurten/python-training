import pytest

from library.solid_examples.ocp import Shape, Rectangle, Circle


class TestShape:

    def test_area_no_errors(self):
        shape = Shape()
        try:
            shape.area()
        except Exception as e:
            pytest.fail(f"Unexpected error: {e}")

    def test_rectangle_area(self):
        rectangle = Rectangle(4, 5)
        assert rectangle.area() == 20

    def test_circle_area(self):
        circle = Circle(3)
        assert circle.area() == 28.26

    def test_rectangle_zero_area(self):
        rectangle = Rectangle(0, 5)
        assert rectangle.area() == 0

    def test_circle_zero_area(self):
        circle = Circle(0)
        assert circle.area() == 0

    def test_circle_large_radius_area(self):
        circle = Circle(1000000)
        assert circle.area() == 3140000000000.0


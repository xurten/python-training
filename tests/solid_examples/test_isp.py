import math
import sys

import pytest

from library.solid_examples.isp import Circle, Rectangle


class TestCircle:

    def test_calculate_area_and_perimeter_radius_1(self):
        circle = Circle(1)
        assert circle.calculate_area() == math.pi
        assert circle.calculate_perimeter() == 2 * math.pi

    def test_calculate_area_and_perimeter_radius_0(self):
        circle = Circle(0)
        assert circle.calculate_area() == 0
        assert circle.calculate_perimeter() == 0

    def test_calculate_area_and_perimeter_large_radius(self):
        circle = Circle(1000)
        assert circle.calculate_area() == math.pi * 1000 ** 2
        assert circle.calculate_perimeter() == 2 * math.pi * 1000

    def test_calculate_area_and_perimeter_negative_radius(self):
        circle = Circle(-1)
        assert circle.calculate_area() == math.pi
        assert circle.calculate_perimeter() == -1*2 * math.pi

    def test_calculate_area_and_perimeter_max_float_radius(self):
        circle = Circle(sys.float_info.max)
        with pytest.raises(OverflowError):
            assert circle.calculate_area() == math.pi * sys.float_info.max ** 2
            assert circle.calculate_perimeter() == 2 * math.pi * sys.float_info.max

    def test_calculate_area_and_perimeter_min_float_radius(self):
        circle = Circle(sys.float_info.min)
        assert circle.calculate_area() == math.pi * sys.float_info.min ** 2
        assert circle.calculate_perimeter() == 2 * math.pi * sys.float_info.min


class TestRectangle:

    def test_create_rectangle_with_positive_width_and_height(self):
        rectangle = Rectangle(5, 10)
        assert rectangle.width == 5
        assert rectangle.height == 10

    def test_calculate_area_with_positive_width_and_height(self):
        rectangle = Rectangle(5, 10)
        assert rectangle.calculate_area() == 50

    def test_calculate_perimeter_with_positive_width_and_height(self):
        rectangle = Rectangle(5, 10)
        assert rectangle.calculate_perimeter() == 30

    def test_create_rectangle_with_zero_width_and_height(self):
        rectangle = Rectangle(0, 0)
        assert rectangle.width == 0
        assert rectangle.height == 0

    def test_create_rectangle_with_negative_width_and_height(self):
        rectangle = Rectangle(-5, -10)
        assert rectangle.width == -5
        assert rectangle.height == -10

    def test_create_rectangle_with_one_dimension_zero(self):
        rectangle = Rectangle(5, 0)
        assert rectangle.width == 5
        assert rectangle.height == 0

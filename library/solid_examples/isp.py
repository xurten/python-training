from abc import ABC, abstractmethod
import math


# 4. Interface Segregation Principle (ISP):
#
# Description:
# The Interface Segregation Principle (ISP) states that a client should not be forced to depend
#                                           on interfaces it does not use. In other words, it's better to have many small,
#                                           specific interfaces rather than one large, general-purpose interface.
#
# Benefits:
#
# Reduced Dependency: Clients are not burdened with unnecessary dependencies on methods they don't need,
#                     leading to cleaner and more modular code.
#
# Flexibility: Implementing interfaces with only the necessary methods allows for more flexibility in designing classes
#              that satisfy specific contracts.
#
# Easier Refactoring: Smaller interfaces are easier to refactor without affecting a large number of clients.

class Shape(ABC):
    @abstractmethod
    def calculate_area(self) -> float:
        pass

    @abstractmethod
    def calculate_perimeter(self) -> float:
        pass


class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius

    def calculate_area(self) -> float:
        return math.pi * self.radius ** 2

    def calculate_perimeter(self) -> float:
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def calculate_area(self) -> float:
        return self.width * self.height

    def calculate_perimeter(self) -> float:
        return 2 * (self.width + self.height)

# 2. Open-Closed Principle (OCP):

# Description:
# The Open-Closed Principle (OCP) states that software entities (such as classes, modules, functions, etc.)
#                                 should be open for extension but closed for modification.
#                                 This means that you should be able to extend the behavior of a system
#                                 without modifying its source code.
#
# Benefits:
#
# Maintainability: Existing code remains stable when new features are added.
#                  This reduces the risk of introducing bugs in the existing codebase.
#
# Scalability: New functionality can be added by creating new classes or modules, rather
#              than modifying existing ones, allowing for easier scaling of the application.
#
# Reusability: Closed code can be reused in different contexts,
#              as long as the extension points (interfaces, abstract classes) are properly designed.

class Shape:
    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2



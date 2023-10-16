import abc
# 3. Liskov Substitution Principle (LSP):

# Description:
# The Liskov Substitution Principle (LSP) states that objects of a superclass
#                                         should be replaceable with objects of its subclasses without affecting
#                                         the correctness of the program. In other words, derived classes should
#                                         be substitutable for their base classes.
#
# Benefits:
#
# Polymorphism: Code can be written to use the base class, and it will work correctly with any derived class.
#               This promotes code flexibility and reuse.
#
# Testability: Substitutable objects make it easier to write unit tests and perform behavior-driven development (BDD).
#
# Design Clarity: Proper adherence to LSP results in a clear and consistent class hierarchy,
#                 making the codebase easier to understand and maintain.

class Bird(metaclass=abc.ABCMeta):
    def __init__(self):
        # initialize any necessary attributes here
        pass

    @abc.abstractmethod
    def fly(self):
        raise NotImplementedError("fly method is not implemented")

    def __str__(self):
        return "I am a bird"


class Penguin(Bird):
    def fly(self):
        print("I can't fly, but I can swim")


def bird_action(bird):
    bird.fly()


# bird = Bird()
# bird_action(bird)

# penguin = Penguin()
# bird_action(penguin)

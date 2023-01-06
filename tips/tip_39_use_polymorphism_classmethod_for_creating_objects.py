# Tip 39 Use polymorphism classmethod for creating objects

# @classmethod vs @staticmethod
# The following table lists the difference
# between the class method and the static method:

# @classmethod	@staticmethod
# Declares a class method. |	Declares a static method.
# It can access class attributes, but not the instance attributes. |	It cannot access either class attributes or instance attributes.
# It can be called using the ClassName.MethodName() or object.MethodName().  |	It can be called using the ClassName.MethodName() or object.MethodName().
# It can be used to declare a factory method that returns objects of the class.  |	It cannot return an object of the class.
# source for the comparison: https://www.tutorialsteacher.com/python/classmethod-decorator
import os


class GenericInputData:
    def read(self):
        raise NotImplementedError

    @classmethod
    def generate_inputs(cls, config):
        raise NotImplementedError


class PathInputData(GenericInputData):

    @classmethod
    def generate_inputs(cls, config):
        data_dir = config['data_dir']
        for name in os.listdir(data_dir):
                yield cls(os.path.join(data_dir, name))

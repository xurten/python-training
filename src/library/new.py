# the property class

class Car:
    def __init__(self, name):
        self._name = name

    def set_name(self, name):
        self._name = name

    def get_name(self):
        return self._name

    name = property(fget=get_name, fset=set_name)


class NewCar:
    def __init__(self, language):
        self._language = language

    @property
    def language(self):
        return self._name


red_car = Car('Red')
print(red_car.name)

print(help(Car))

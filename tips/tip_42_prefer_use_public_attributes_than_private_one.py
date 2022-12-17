# Tip 42 prefer to use public attributes than the private ones

# example of a class with private instance variable
class PrivateObject:
    def __init__(self):
        self.__private_field = 10

    def get_private_field(self):
        return self.__private_field


# example of a class with protected instance variable
class ProtectedObject:
    def __init__(self, protected_field):
        self._protected_field = protected_field

    @property
    def protected_field(self):
        return self._protected_field

    @protected_field.setter
    def protected_field(self, protected_field):
        self._protected_field = protected_field


# example of a class with public instance variable
class PublicObject:
    def __init__(self):
        self.public_field = 5

    def get_public_field(self):
        return self.public_field

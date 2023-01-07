# Tip 40 initialization of the parent class with super
# MRO - method resolution order, superclass will be called only once

class MyBaseClass:
    def __init__(self, value):
        self.value = value


class MyChildClass(MyBaseClass):
    def __init__(self):
        MyBaseClass.__init__(self, 5)


class ImplicitTrisect(MyBaseClass):
    def __init__(self, value):
        super().__init__(value)

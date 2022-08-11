# object contain state and behaviour
# everything is a object, callable
number = 1
print(type(number))
print(type(1111))


class MyClass:
    def __init__(self, value):
        self.value = value
        pass

    language = 'pl'
    age = 10
    __class__ = str
    pass

    def hello(self):
        print("aaaa")
        print(f'{MyClass.language}')


class MySecondClass:
    def hello(self):
        print(f'{MyClass.language} {self.var}')


from types import MethodType

aaa = MySecondClass()
aaa.hello_new = MethodType(lambda self: 'Hello world', aaa)


print(type(MySecondClass))
a = MySecondClass()
print(type(a))
print(MyClass.__name__)
value = getattr(MyClass, 'age', 'None')
# setattr, delattr, del, instance attribute
print(value)
# mapping proxy object, just a property of a object
# each object has it own namespace, instance namespace
print(MyClass.__dict__)
print(f' empty = {a.__dict__}')
print(MySecondClass.hello)
print(a.hello.__func__)
# method object
# obj.method(param) == method.__func__(method.__self__, params)
# method should to be bound to something, instance method
print(a.__dict__)

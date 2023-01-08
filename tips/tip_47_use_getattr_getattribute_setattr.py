# Tip 47 use method __getattr__(), __getattribute__() , __setattr__()
# __getattr__() is called once, when the attribute does not exist
# __getattribute__() is always called during access to class attribute

class LazyRecord:
    def __init__(self):
        self.exists = 5

    def __getattr__(self, item):
        value = 3
        setattr(self, item, value)
        return value


data = LazyRecord()
print(data.__dict__)
print(hasattr(data, 'foo'))
print(data.foo)
print(data.__dict__)

# Tip 85 use packages to organize modules and provide stable APIs
# python packages has two primary goals:
# - namespaces
# - stable API
# use as keyword for similar packages
# attribute __all__, all public methods you can import, if you specify it in file
# you can select which methods, objects you can allow for import from other packages, if
# no then all public elements are accessible

import io
from io import open as new_open

__all__ = ['simulate']
# use as
print(new_open)
print(type(new_open))

# full path
print(io.open)


class Project:
    pass


def _dot_product():
    pass


def simulate():
    pass

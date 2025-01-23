# better error message with tips
from typing_extensions import TypedDict, ReadOnly

print("better error message".split(maxsplit=2))
# update for math library
from math import fma
print(fma(1,2,4))
class Point2D(TypedDict):
    x: float
    y: float
    label: ReadOnly[str]

point = Point2D(x=10,y=20,label='A')
print(point)
point["x"] = 20
point['label'] = 'hello'
print(point)
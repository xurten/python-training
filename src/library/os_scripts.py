import os
import sys

print(os.name)
sys.path
# print all env fields
for key, val in enumerate(os.environ.items()):
    print(key, " : ", val[0], val[1], type(val))
# print project path
print(sys.path[0])

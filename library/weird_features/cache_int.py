# python cache small int for performance reasons
a = int("256")
b = int("256")

print(a is b)

a = int("257")
b = int("257")
# different objects
print(a is b)

a = 256
b = 256

print(a is b)

a = 257
b = 257

print(a is b)

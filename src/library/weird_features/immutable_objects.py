data = (1, 2)
print(data)
try:
    data[0]+= 1
except Exception as e:
    print(e)
    print(data)

data = ([1],2)
print(data)
try:
    data[0]+=[3]
except Exception as e:
    print(e)
    print(data)
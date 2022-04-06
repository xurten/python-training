# Comprehension List
x = [i for i in range(10)]
print(x)
# Comprehension Dictionary
y = {i: i + 2 for i in range(4)}
print(y)
# Slicing [start:end:step]
print(x[0:5:1])
# Lambda function
sum = lambda x, y: x + y
print(sum(1000,2000))
# Reverse copy of array and list
import array as arr
my_array = arr.array('i', [1,2,3,4,5])
print(my_array[::-1])
print([i for i in range(20)][::-1])


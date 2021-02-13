# Write a Python program to square and cube every number in a given list of integers using Lambda.


lis = list(range(1, 21))
result1 = list(map(lambda x: x ** 2, lis))
print("Squaring every number of lis")
print(result1)
result2 = list(map(lambda x: x ** 3, lis))
print("Cubing every number of lis")
print(result2)

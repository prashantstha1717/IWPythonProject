# Write a Python program to filter a list of integers using Lambda.

lis = list(range(1, 21))
result = filter(lambda x: x % 2 == 0, lis)
print("Evens Numbers: ")
print(list(result))
result1 = filter(lambda x: x % 2 != 0, lis)
print("Odd Numbers: ")
print(list(result1))

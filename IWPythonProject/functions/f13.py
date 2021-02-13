# Write a Python program to sort a list of tuples using Lambda.


lis = [(1, 2), (4, 8), (8, 3), (2, 4)]
print(f"Sorting from first element of tuple")
lis.sort(key=lambda x: x[0])
print(lis)
lis.sort(key=lambda x: x[1])
print(f"Sorting from second element of tuple")
print(lis)
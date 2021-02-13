# Write a Python program to multiply all the items in a dictionary.

my_dict = {1: 10, 2: 20, 3: 30, 4: 40, 5:50}
result = 1

for key in my_dict:
    result = result * my_dict[key]


print(result)

# Write a Python program to iterate over dictionaries using for loops.

def out31(dic):
    for key, value in dic.items():
        print(f'{key}: {value}')


out31({0: 10, 1: 20, 2: 30})
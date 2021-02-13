# Write a Python program to iterate over dictionaries using for loops.

def out35(dic):
    for key, value in dic.items():
        print(f'{key}: {value}')


out35({0: 10, 1: 20, 2: 30})
# Write a Python program to remove the nth index character from a non empty string.

def out8(string):
    lis = list(string)
    n = int(input('type the index of alphabet: '))
    lis.pop(n)
    return ''.join(lis)


print(out8('Insight Workshop'))

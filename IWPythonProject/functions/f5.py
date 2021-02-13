# Write a Python function to calculate the factorial of a number (a non-negative
# integer). The function accepts the number as an argument.
from functools import reduce


def f5(num):
    if num == 0:
        return 1
    else:
        return num * f5(num-1)


number = int(input("Enter a non negative number: "))
print(f5(number))
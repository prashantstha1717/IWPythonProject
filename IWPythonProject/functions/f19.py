# Write a Python program to create Fibonacci series upto n using Lambda.

from functools import reduce


def fibonacci(count):
    sequence = (0, 1)

    for _ in range(2, count):
        sequence += (reduce(lambda a, b: a + b, sequence[-2:]), )

    return sequence


print(fibonacci(7))
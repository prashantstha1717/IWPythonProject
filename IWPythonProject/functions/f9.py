# Write a Python function that takes a number as a parameter and check the
# number is prime or not.

def f9(num):
    if num == 1:
        return f'{num} is not a prime number'
    else:
        for i in range(2, num):
            if num % i == 0:
                return f'{num} is not a prime number'
    return f"{num} it is prime number"


number = int(input("Enter a number: "))
print(f9(number))

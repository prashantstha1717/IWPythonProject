# Write a Python function to check whether a number is in a given range.

def f6(num):
    if num in range(10):
        return f'Congratulations!!!! Number you entered is in the range'
    else:
        return f'Sorry the number you entered is not in the range'


n = int(input("Enter the number: "))
print(f6(n))

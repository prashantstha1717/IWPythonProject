# . Write a Python function that accepts a string and calculate the number of
# upper case letters and lower case letters.
# Sample String : 'The quick Brow Fox'
# Expected Output :
# No. of Upper case characters : 3
# No. of Lower case Characters : 12

def f7(sample):
    upper = 0
    lower = 0
    for char in sample:
        if char.isupper():
            upper += 1
        elif char.islower():
            lower += 1
    print(f'Number of upper case letters: {upper}')
    return f'Number of lower case letters: {lower}'


print(f7('The quick Brow Fox'))


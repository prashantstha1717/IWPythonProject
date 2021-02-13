# Write a Python program to count the number of characters (character frequency) in a string.

# Sample String : google.com'

# Expected Result : {'o': 3, 'g': 2, '.': 1, 'e': 1, 'l': 1, 'm': 1, 'c': 1}

sample1 = 'google.com'
out1 = {}

for char in sample1:
    if char in out1:
        out1[char] += 1
    else:
        out1[char] = 1

print(out1)

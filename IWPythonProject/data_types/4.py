# Write a Python program to get a single string from two given strings, separated
# by a space and swap the first two characters of each string.

# Sample String : 'abc', 'xyz'
# Expected Result : 'xyc abz'

def out4(lis):
    first_two_letter1 = lis[0][:2]
    first_two_letter2 = lis[1][:2]
    char1 = first_two_letter2 + lis[0][-1]
    char2 = first_two_letter1 + lis[1][-1]
    return char1 + ' ' + char2


print(out4(['abc', 'xyz']))

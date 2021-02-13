# Write a Python program to insert a given string at the beginning of all items in
# a list.
# Sample list : [1,2,3,4], string : emp
# Expected output : ['emp1', 'emp2', 'emp3', 'emp4']


def out26(sample, string):
    string += '{0}'
    sample = [string.format(i) for i in sample]
    return sample


sample = [1, 2, 3, 4]
string = 'emp'

print(out26(sample, string))
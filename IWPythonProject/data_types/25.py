#  Write a Python program to check whether all dictionaries in a list are empty or
# not.
# Sample list : [{},{},{}]
# Return value : True
# Sample list : [{1,2},{},{}]
# Return value : False

sample1 = [{}, {}, {}]
sample2 = [{1, 2}, {}, {}]
print(all(not d for d in sample1))
print(all(not d for d  in sample2))



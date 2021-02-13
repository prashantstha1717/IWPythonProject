# Write a Python program to find if a given string starts with a given character using Lambda.
char = str(input("Enter a string: "))
word = "apple"
result = lambda x: True if x.startswith(char) else False
print(result(word))

# Write a Python program to count the occurrences of each word in a given sentence.

sample = 'When I was a little boy I wanted to be a hero. Not some damn business man. But a superhero who could send ' \
         'rotten villains like you flying with one punch. '


def out11(string):
    count = {}
    li = string.split(' ')
    for words in li:
        if words in count:
            count[words] += 1
        else:
            count[words] = 1
    return count


print(out11(sample))
# Write a Python program to find the first appearance of the substring 'not' and
# 'poor' from a given string, if 'not' follows the 'poor', replace the whole 'not'...'poor'
# substring with 'good'. Return the resulting string.

# Sample String : 'The lyrics is not that poor!'
# 'The lyrics is poor!'
# Expected Result : 'The lyrics is good!'
# 'The lyrics is poor!

def out6(str1):
    nots = str1.find('not')
    poors = str1.find('poor')
    if poors > nots and nots > 0 and poors > 0:
        str1 = str1.replace(str1[nots:(poors + 4)], 'good')
        return str1
    else:
        return str1


print(out6('The lyrics is not that poor'))

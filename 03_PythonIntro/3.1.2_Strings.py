print('spam eggs')  # single quotes

print('doesn\'t')  # use \' to escape the single quote...

print("doesn't")  # ...or use double quotes instead

print('"Yes," they said.')

print("\"Yes,\" they said.")

print('"Isn\'t," they said.')

print('"Isn\'t," they said.')

print('"Isn\'t," they said.')

s = 'First line.\nSecond line.'  # \n means newline

print(s)  # with print(), \n produces a new line

#print('C:\some\name')  # here \n means newline! Comment this to run this script

print(r'C:\some\name')  # note the r before the quote

print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")

# 3 times 'un', followed by 'ium'
print( 3 * 'un' + 'ium' )

print('Py' 'thon')

text = ('Put several strings within parentheses '
         'to have them joined together.')

print(text)

prefix = 'Py'

#print(prefix 'thon')    # can't concatenate a variable and a string literal

#print(('un' * 3) 'ium') # can't concatenate a variable and a string literal

#for concatenating variable and literal use +

print(prefix + 'thon')

print(('un' * 3) + 'ium')

#positive indices to start counting from left as normally done
word = 'Python'
print(word[0])
print(word[5])

#negative indices to start counting from right
print(word[-1])
print(word[-2])
print(word[-6])

print(word[0:2])  # characters from position 0 (included) to 2 (excluded)
print(word[2:5])  # characters from position 2 (included) to 5 (excluded)

#slice indices left omission is 0, right omission is length of string
print(word[:2] + word[2:])

print(word[:4] + word[4:])

print(word[:2])

print(word[4:])

print(word[-2:])

#word[42]  # the word only has 6 characters, hence will error out

#but slice indices handle the above exception gracefully

print(word[4:42])

print(word[42:])

#strings are immutable
#word[0] = 'J' Wont work

#word[2:] = 'py' Wont work

#if a new string is needed, we need to create a new one
print('J' + word[1:])

print(word[:2] + 'py')

s = 'Aritra Chatterjee'
print(len(s))
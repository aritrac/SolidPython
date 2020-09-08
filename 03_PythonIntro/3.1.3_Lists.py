squares = [1, 4, 9, 16, 25]
print( squares)

print(squares[0])

print(squares[-1])

print(squares[-3:])

print(squares[:])

#We can concatenate two lists
print(squares + [36,49,64,81,100])

#Unlike strings, lists are mutable
cubes = [1, 8, 27, 65, 125]  # we will update the fourth index

print (cubes)

cubes[3] = 64

print(cubes)

cubes.append(216)  # add the cube of 6

print(cubes)

cubes.append(7 ** 3) #add cube of 7

print(cubes)

#Assignment to slices is also possible, and this can even change the size of the list or clear it entirely

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(letters)

# replace some values
letters[2:5] = ['C', 'D', 'E']
print(letters)

# now remove them
letters[2:5] = []
print(letters)

# clear the list by replacing all the elements with an empty list
letters[:] = []
print(letters)

print(len(letters))

#It is possible to nest lists (create lists containing other lists), for example
a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
print(x)

print(x[0])

print(x[0][1])

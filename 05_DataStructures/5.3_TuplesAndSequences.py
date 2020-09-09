t = 12345, 54321, 'hello!'

print(t[0])

print(t)

# Tuples may be nested:
u = t, (1, 2, 3, 4, 5)

print(u)

#Tuples are immutable:
#t[0] = 88888 #This will error out

#but they can contain mutable objects:
v = ([1, 2, 3], [3, 2, 1])

print(v)

empty = ()

singleton = 'hello',    # <-- note trailing comma, so it is not a string

print(len(empty))

print(len(singleton))

print(singleton)

#t = 12345, 54321, 'hello!' #Tuple packing

#Tuple unpacking

x,y,z = t

print(x)
print(y)
print(z)

def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)

ask_ok('Do you really want to quit?')
ask_ok('OK to overwrite the file?', 2)
ask_ok('OK to overwrite the file?', 2, 'Come on, only yes or no!')

#The default values are evaluated at the point of function definition in the defining scope

i = 5

def f(arg=i):
    print(arg)

i = 6
f()  #This will print 5 and not 6

#The default value is evaluated only once. This makes a difference when the default is a mutable object such as a 
#list, dictionary, or instances of most classes.
def f2(a, L=[]):
    L.append(a)
    return L

print(f2(1))
print(f2(2))
print(f2(3))

#If you don’t want the default to be shared between subsequent calls, you can write the function like this instead
def f3(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L

print(f3(1))
print(f3(2))
print(f3(3))
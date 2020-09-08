def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")

parrot(1000)                                          # 1 positional argument
parrot(voltage=1000)                                  # 1 keyword argument
parrot(voltage=1000000, action='VOOOOOM')             # 2 keyword arguments
parrot(action='VOOOOOM', voltage=1000000)             # 2 keyword arguments
parrot('a million', 'bereft of life', 'jump')         # 3 positional arguments
parrot('a thousand', state='pushing up the daisies')  # 1 positional, 1 keyword

#invalid function calls
#parrot()                     # required argument missing
#parrot(voltage=5.0, 'dead')  # non-keyword argument after a keyword argument
#parrot(110, voltage=220)     # duplicate value for the same argument
#parrot(actor='John Cleese')  # unknown keyword argument

#No function arguments should receive 2 values
def example(a):
    pass

# example(0, a=0) This wont work

#When a final formal parameter of the form **name is present, it receives a dictionary (see Mapping Types — dict) 
# containing all keyword arguments except for those corresponding to a formal parameter. This may be combined with a 
# formal parameter of the form *name (described in the next subsection) which receives a tuple containing the positional 
# arguments beyond the formal parameter list. (*name must occur before **name.)

def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])

cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")

# def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
#       -----------    ----------     ----------
#         |             |                  |
#         |        Positional or keyword   |
#         |                                - Keyword only
#          -- Positional only

def standard_arg(arg):
    print(arg)

def pos_only_arg(arg, /):
    print(arg)

def kwd_only_arg(*, arg):
    print(arg)

def combined_example(pos_only, /, standard, *, kwd_only):
    print(pos_only, standard, kwd_only)

standard_arg(2)
standard_arg(arg=2)

pos_only_arg(1)
#pos_only_arg(arg=3) This will not work as this method only accepts positional params

#kwd_only_arg(3) This will not work as this method only accepts keyword params
kwd_only_arg(arg=3)

#combined_example(1,2,3) Wont work as 3 positional args were given instead of 2
combined_example(1,2,kwd_only=3)
combined_example(1,standard=2,kwd_only=3)
#combined_example(pos_only=1, standard=2,kwd_only=3) This wont work as no positional args were given, and the method expects
#atleast 1 positional param.

#Finally, consider this function definition which has a potential collision between the positional argument name and **kwds which has name as a key:
def foo(name, **kwds):
    return 'name' in kwds

#There is no possible call that will make it return True as the keyword 'name' will always bind to the first parameter. For example:
#print(foo(1, **{'name': 2})) It will complain of getting multiple values for argument name

#But using / (positional only arguments), it is possible since it allows name as a positional argument and 'name' as a key in the keyword arguments:
def foo2(name, /, **kwds):
    return 'name' in kwds

print(foo2(1,**{'name':2}))
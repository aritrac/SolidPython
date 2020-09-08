#The least frequently used option is to specify that a function can be called with an arbitrary number of 
#arguments. These arguments will be wrapped up in a tuple

def write_multiple_items(file, separator, *args):
    file.write(separator.join(args))

#Any formal parameters which occur after the *args parameter are ‘keyword-only’ arguments
def concat(*args, sep="/"):
    return sep.join(args)

print(concat("earth", "mars", "venus"))

print(concat("earth", "mars", "venus", sep="."))
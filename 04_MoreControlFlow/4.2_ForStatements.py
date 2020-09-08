# Measure some strings:
words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))

# Strategy:  Iterate over a copy
users = {}
for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]

# Strategy:  Create a new collection
active_users = {}
for user, status in users.items():
    if status == 'active':
        active_users[user] = status

#This is strange
print(range(10)) #Just prints range(0,10)

print(sum(range(4))) #prints the sum

print(list(range(4))) #prints out a list from 0 to 3
users = ['Kristine', 'Tiffany', 'Jordan', 'Leann']

print(users)

users.remove('Jordan') #only removes one element

print(users)

popped_user  = users.pop() #removes very last item, and returns the item so you can use it. Grabbing the item at the end.

print(popped_user)
print(users)

del users[0] #straight deletes the item specified

print(users)
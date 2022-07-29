"""
User Database Query
Kristine
Tiffany
Jordan
"""

users = ['Kristine', 'Tiffany', 'Jordan']

print(users)

users.insert(0, 'Anthony') #number is the spot you are placing the element at starting with 0 up to whatever. To change it just change the number / Super simple

print(users)

users.append('Ian') #.append adds to the end of the list

print(users)

print(users[2]) #returns the string at whatever spot its at, if you put brackets like this 'print([users[2]])' itll turn out like [Tiffany].

users[4] = 'Brayden' #string gets reassigned NOT changed

print(users)
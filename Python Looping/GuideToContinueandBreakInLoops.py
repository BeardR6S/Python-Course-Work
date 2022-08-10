usernames = [
    'jon',
    'tyrion',
    'theon',
    'cersei',
    'sansa',
]

#Continue / Break


#This is Continue

# for username in usernames:
#     if username == 'cersei':
#         print(f'Sorry, {username}, You are not allowed')
#         continue
#     else:
#         print(f'{username} is allowed')

#This is Break

for username in usernames:
    if username == 'cersei':
        print(f'{username} was found at index {usernames.index (username)}')
        break
    print(username)
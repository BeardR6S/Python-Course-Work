users = ['Kristine', 'Tiffany', 'Jordan', 'Leann']

ids = [1, 2, 3, 4]

mixed_list = [42, 10.3, 'Altuve', users] #be very careful, If you are adding stuff up to a sum, adding a word or list of lists with words, itll break the program.

print(mixed_list)

user_list = mixed_list.pop() #.pop() returns the last element, whether a list or an item or whatever.

print(user_list)
print(mixed_list)


nested_list = [[123], [234], [345]]

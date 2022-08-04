from decimal import Decimal 
import math
from xml.etree.ElementPath import xpath_tokenizer_re

#Exercise 1: Create a list, tuple, float, integer, decimal, and dictionary.

This_is_my_list = ['Hi', 'Hello', 'Sup', 'Bonjour'] #Mutable

This_is_my_tuple = ('This', 'Is', 'Immutable') #Immutable

Part_3 = float(59.7)

integer = 893945873

y = .61839367482363826738327636356252
Example_here = Decimal(y)
print(Example_here)

Dict = {
    'One': "Hello",
    'Two': "Good-Bye",
    'Three': 'Development',
    'Four': 'Example',
    'Five': 'Python',
}

#Exercise 2: Round your float up.

print(round(Part_3))

#Exercise 3: Get the square root of your float.

print(math.sqrt(Part_3))

# Exercise 4: Select the first element from your dictionary.

Dict = {
    'One': 'Hello',
    'Two': 'Good-Bye',
    'Three': 'Development',
    'Four': 'Example',
    'Five': 'Python',
}

x = Dict.get('One')

print(x)

#Exercise 5: Select the second element from your tuple.

This_is_my_tuple = ('This', 'Is', 'A', 'Tuple')

print(This_is_my_tuple[1])

#Exercise 6: Add an element to the end of your list.

This_is_my_list = ['Hi', 'Hello', 'Sup', 'Bonjour']

added_element = This_is_my_list + ['Guten Morgen']

print(added_element)

#Exercise 7: Replace the first element in your list.

This_is_my_list = ['Hi', 'Hello', 'Sup', 'Bonjour']

This_is_my_list[0] = 'Hola'

print(This_is_my_list)

#OR

This_is_my_list = ['Hi', 'Hello', 'Sup', 'Bonjour']

This_is_my_list.insert(0, 'Hola')

print(This_is_my_list)

#Exercise 8: Sort your list alphabetically.

This_is_my_list = ['Hi', 'Hello', 'Sup', 'Bonjour']

This_is_my_list.sort()

print(This_is_my_list)

#OR

This_is_my_list = ['Hi', 'Hello', 'Sup', 'Bonjour']

sorted_list = sorted(This_is_my_list)

print(sorted_list)

#Exercise 9: Use reassignment to add an element to your tuple.

This_is_my_tuple = ('This', 'Is', 'Immutable',)

This_is_my_tuple += ('I Promise',)

print(This_is_my_tuple)
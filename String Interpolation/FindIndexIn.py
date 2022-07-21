#Finding a Substring in Python with: Find, Index, and In

sentence = 'The quick brown fox jumped over the lazy dog.'

#query = sentence.find('quick')
#pulls the number 4, its the 4th letter, start at t=0/ If not found returns a -1

#query = sentence.index('quick')
#be careful when using index, Index with throw an error if it cant find something, where find with just return a "-1"

#query = 'fox' in sentence
#returns "True" if its there, "False" if it isnt. This is Industry Standard/Most common way.

query = 'oops' in sentence #returns False as oops is not in the sentence.

print(query)
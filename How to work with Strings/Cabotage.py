# The quick brown fox jumped
# T => 0
# h => 1
# e => 2
#' ' => 3

starter_sentence = 'The quick brown fox jumped' 
# first_word = starter_sentence[0:2] #ends at the item BEFORE the last number in the []
new_sentence = 'Thy' + starter_sentence[3:] #if you do [Number:] Python thinks you want to go all the way to the end of the sentence.
print(new_sentence)



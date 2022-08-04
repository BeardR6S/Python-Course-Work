post = ('Python Basics', 'Intro guide to python', 'Some cool python content', 'Published')

#How to remove items from end of tuple

# post = post[:-1] #removes everything right of the element you selected including the selected element.


#removing elemeents from beginning

# post = post[2:] #removes everything left of the element you selected including the selected element.

#removing specific element (messy/not recommended)

post = list(post)
post.remove('Published') #[] shows it changed to a list
post = tuple(post) #() shows it changed back to tuple

print(post)
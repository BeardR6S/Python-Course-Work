#to add to tuple, make sure to include , at the end of the item in ().

post = ('Python Basics', 'Intro guide to Python', 'Some cool python content')


print(id(post))

post += ('Published',)

print(id(post))
# title, sub_heading, content, status = post

# print(title)
# print(sub_heading)
# print(content)
# print(status)
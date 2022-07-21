#Heredoc

# content = """
# Nullam id dolor id nibh ultricies vehicula ut id elit. Nullam quis risus eget urna mollis ornare vel eu leo.

# Vestibulum id ligula porta felis euismod semper. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Cras justo odio, dapibus ac facilisis in.

# Integer posuere erat a ante venenatis dapibus posuere velit aliquet.
# """.strip() #.strip helps remove extra lines of space in the front and back of something when its ran.


# content = """
# Nullam id dolor id nibh ultricies vehicula ut id elit. Nullam quis risus eget urna mollis ornare vel eu leo.

# Vestibulum id ligula porta felis euismod semper. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Cras justo odio, dapibus ac facilisis in.

# Integer posuere erat a ante venenatis dapibus posuere velit aliquet.
# """


# print(repr(content)) #shows new line character which is how a computer seperates the lines \n is what it puts when a new line starts. Double \n is a end of a line and a empty line.


long_string = '\nNullam id dolor id nibh ultricies vehicula ut id elit. Nullam quis risus eget urna mollis ornare vel eu leo.\n\nVestibulum id ligula porta felis euismod semper. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Cras justo odio, dapibus ac facilisis in.\n\nInteger posuere erat a ante venenatis dapibus posuere velit aliquet.\n'

print(long_string)
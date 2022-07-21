#partition function
#use an underscore for anything you dont want to use. Not required, but best practice.
#returns a tuple

from colorsys import TWO_THIRD


heading = "Python: An Introduction"

# header, _, subheader = heading.partition(': ')

# print(header)
# print(subheader)

first, second, third = heading.partition(': ')

print(first)
print(third)
print(second)
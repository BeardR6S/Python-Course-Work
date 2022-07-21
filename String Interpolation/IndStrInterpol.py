#How to Use Python's format method to Implement Index Based String Interpolation
#Can be used instead of having to type out the element, Look below and run it to see what happens if confused.

name = 'Johnny'
age = 47
product = 'Python eLearning Course'
from_account = 'Brandon'

# greeting = "Hi {0}, you are listed as {1} years old and you have purchased: {2}. Congrats on taking your first step to a new career {0}.".format(name, age, product)

greeting = f"Product Purchase: {product} - Hi {name}, you are listed as {age} years old. - {from_account}" 
#This is better, as you dont have to count it out and can see the name of what you are showing.

print(greeting)
"""
Write a program that prints the numbers from 1 to 100 but for multiples of 3 it prints Fizz. 
So it prints a string of fizz instead of the number and for the multiples of five it prints Buzz. 
For the numbers which are multiples of both 5 and 3 then you're going to print out fizz buzz.
------------------------------------
Example Below-
1
2
'Fizz'
4
'Buzz'
...
'FizzBuzz' = 15

Tools you can use
-Fuction
-Looping
-Conditionals
-Math Operators
"""

#-----------------------------------

#Wrong

# for i in range (1, 101):
#     if i%3==0:
#         print('Fizz')
#     elif i%5==0:
#         print('Buzz')
#     elif i%3==0 and i%5==0:
#         print('FizzBuzz')

# else:
#     print(i)

#-----------------------------------

#Works
# for i in range(1, 101):
#     if i%3==0 and i%5==0:
#         print('FizzBuzz')
#     elif i%3==0:
#         print('Fizz')
#     elif i%5==0:
#         print('Buzz')

#     else:
#         print(i)

#----------------------------------
#Also Works

# for i in range(1, 101):
#     output = ''
#     if i%3==0:
#         output = 'Fizz'
#     if i%5==0:
#         output += 'Buzz'
    
#     print(output or i)
    
#--------------------------------
#Also Works (turnary operators)

# for i in range(1, 101):

#     output = 'Fizz' if i%3==0 else ''
#     output = 'Buzz' if i%5==0 else ''  

#     print(i) if output=='' else print(output)   

#-------------------------------
#Also Works in one line of code

for i in range(1, 101):
    print('Fizz'*(i%3<1)+(i%5<1)*'Buzz' or i)
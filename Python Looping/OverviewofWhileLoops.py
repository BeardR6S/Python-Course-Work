#With a for-in loop you have a very clearly defined start and finish to your loop. 
#So if you're looping over a list of strings when you're done iterating through the entire list the for-in loop just completely stops and that is the type of behavior that you want for it.

#While Loop won't stop unless you include a sentinel value

# nums = list(range(1,100))

# while len(nums) > 0:
#     print(nums.pop())

def guessing_game():
    while True:
        print('What is your guess?')
        guess = input()

        if guess == '42':
            print('You correctly guessed it!')
            return False
        else:
            print(f'No, {guess} is not the answer, please try again\n')

guessing_game()
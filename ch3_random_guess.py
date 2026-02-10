import random

# get the range
small_num = 1
big_num = 100

# get a random number from the random 
target = random.randint(1, 100)

# greet the user 
print(
"""
Random Guess Game!
Guess a number from 1-100!
""")
# set the amount of tries for user
tries = 20
attempts = 0
# create a while loop for game looping
while True:
    # increment attempts
    attempts += 1
    # tell the user how much tries they have left
    print ("You have %0.0f tries" % tries)

    # ask them to guess a number, then store it on guessed_number
    guessed_number = int(input("Please guess a number!: "))

    # create a conditional statement to check user's guessed number
    if guessed_number > target: # if the number is greater than the target, then they guessed too high
        print ("Number is too high!")
    elif guessed_number < target: # if the number is less than the target, then they guessed too low
        print ("Number is too low")
    else: # which means by default, the last case would be if they did guess the number
        print ("You have guessed the number!")
        # tell the user how many tries it took them!
        print ("You guessed the number in %0.0f tries" % attempts)
        break

    # if they didn't guess the number, decrement the variable
    tries -= 1

    # if they reach zero tries, then they have used up all 20 guesses
    if tries == 0:
        print("Game over! The number was %0.0f" % target)

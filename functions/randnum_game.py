# 20. Random Number Guessing Game

# Imports
import random
# Functions
def status(guess):
    if (guess == random):
        print("Wow! You guess correctly.")
    else:
        count = 0
        while (guess != random):
            if guess < random :
                print("Too low, try again.")
            else:
                print("Too high, try again.")
            count += 1
            guess = int(input("Guess:"))
        print("You finally got it!")
        print("It took you",count,"guesses.")

# Program
random = random.randint(1,100)
#print(random)
guess = int(input("Guess the number: "))
status(guess)

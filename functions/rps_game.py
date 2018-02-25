# 21. Rock, Paper, Scissors Game

# Imports
import random
# Functions
def opponent_generate():
    key = random.randint(1,3)
    if key == 1:
        oppChoice = "rock"
    elif key == 2:
        oppChoice = "paper"
    else:
        oppChoice = "scissors"

    return oppChoice

def winner(a,b):
    if a == "rock":
        if b == "rock":
            print("Tie")
        elif b == "paper":
            print("Computer wins!")
        else:
            print("You win!")
    elif a == "paper":
        if b == "rock":
            print("You win!")
        elif b == "paper":
            print("Tie")
        else:
            print("Computer wins!")
    else:
        if b == "rock":
            print("Computer wins!")
        elif b == "paper":
            print("You win!")
        else:
            print("Tie")
# Program
opponentChoice = opponent_generate()
userChoice = str(input("Enter your choice: "))
print(opponentChoice)
winner(userChoice,opponentChoice)

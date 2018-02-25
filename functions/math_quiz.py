# 11. Math Quiz

# Import modules
import random
# ===========================
# Define the function(s)

def quiz(num1,num2):
    print(" ",num1,"\n+",num2,"\n-----")

def generate():
    num1 = random.randint(0,100)
    num2 = random.randint(0,100)
    return num1,num2

def validity(ans):
    if num1 + num2 == ans :
        print("Correct!")
    else:
        print("Wrong.")
# =============================
# Simple code to run.

num1, num2 = generate()
quiz(num1,num2)
ans = int(input(""))
validity(ans)

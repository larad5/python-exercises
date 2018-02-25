# 16.Odd/Even Counter

# Imports
import random

# Functions
def even_odd(num):
    print(num)
    if num % 2 == 0 :
        result = "Even"
    else:
        result = "Odd"
    return result

def generate():
    num = random.randint(0,1000)
    return num

# Program
print(even_odd(generate()))

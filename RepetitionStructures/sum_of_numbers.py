# 8.Sum of Numbers

# ask the user for the first number
number = int(input("Enter positive numbers:\n"))
total = 0

# repetition structure to sum up all the valid numbers entered
while number >= 0:
    total += number
    number = int(input())

# display the sum of all the positive numbers entered
print("----------\nThe sum is", total)

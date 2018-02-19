# 3 Budget Analysis

# ask the user for their montly budget
budget = float(input("What is your budget this month? "))

# repetition structure to collect all of the users expenses
total = 0
exp = float(input("Start entering your expenses: "))
while exp != 0 :
    total += exp
    exp = float(input("Next expense: "))

# decision structure to see if user is over/under budget
if total > budget :
    print("You're over budget this month.")
else:
    print("You're under budget this month.")

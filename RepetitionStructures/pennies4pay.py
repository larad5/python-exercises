# 7.Pennies for Pay

# ask the user for the number of days
days = int(input("How many days did you work? "))
yesterday = 0
total = 0
print("Day\tEarned\n---------------------")
# repetition loop to calculate the salary earned per day and the aggregate amount
for x in range(1, days+1):
    if x == 1:
        today = 0.01
        yesterday = today
        print(x, '\t$', today,sep='')
        total += today
    else:
        today = yesterday * 2
        print(x,"\t$", today,sep='')
        yesterday = today
        total += today

print("You've earned a total of $",total,sep='')

# 1. Bug Collector

#  repetition structure to ask the user to enter the number of bugs collected on each of the 5 days
count = 0
for num in [1, 2, 3, 4, 5]:
    if num == 1 :
        day = int(input("Enter the number of bugs caught on each day:\n" ))
    else:
        day = int(input(""))
    count += day
    
# display the total number of bugs collected after the 5 days
print("You caught", count, "bugs over the 5 day period.")

# 15. Time Calculator

# ask the user to enter a number of seconds
seconds = int(input("Enter an amount of seconds: "))

# determine how to display the seconds depending on the quantity
if seconds < 60 :
    print("You entered", seconds, "seconds.")
elif seconds >= 60 :
    minutes = seconds / 60
    if seconds >= 3600 :
        hours = minutes / 60
        if seconds >= 86400 :
            days = hours / 24
            print("You entered", int(days), "days worth of seconds.")
        else:
            print("You entered", int(hours), "hours worth of seconds.")
    else:
        print("You entered", int(minutes), "minutes worth of seconds.")

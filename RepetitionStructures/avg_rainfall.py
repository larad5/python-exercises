# 5.AVerage Rainfall

# ask for the number of years
years = int(input("Enter the number of years for calculations: "))
rainSum = 0
# outer loop for years
i = 1
while i <= years :
    #inner loop for 12 months in the year
    print("----------\nYear",i)
    print("Enter the rainfall for each month.")
    for x in ["JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"]:
        # ask the user for the inches of rainfall for each month
        inch = int(input(x + ": "))
        rainSum += inch
    i += 1

# display total number of months
months = years * 12
#print(months)
# display total inches of rainfall
#print(rainSum)
# display the average rainfall per month for the entire period
avgRain = rainSum/months
#print(avgRain)

# display results
print("For", months, "months, there was", rainSum, "inches of rain.")
print("The average rainfall over that time was", avgRain, "inches per month.")

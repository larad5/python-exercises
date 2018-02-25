# 19.Future Values

# Imports

# Functions
def mature_value(a,b,c):
    mVal = a * ((1 + b) ** c)
    return mVal

# Program
acctValue = float(input("Account value: "))
intRate = float(input("Interest Rate: "))
months = int(input("Months in account: "))

print(format(mature_value(acctValue,intRate,months),'.2f'))

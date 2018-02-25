# 4.Automobile Costs

# If variables are within a function are locale, how would you make a function
# that gathers more than one variable to be used outside of the function?
e1 = float(input("Loan payment: "))
e2 = float(input("Insurance: "))
e3 = float(input("Gas: "))
e4 = float(input("Oil: "))
e5 = float(input("Tires: "))
e6 = float(input("Maintenance: "))

# Argument names don't need to be the actual variable names that are going to
# be used for the function.
def monthly_costs(e1, e2, e3, e4, e5, e6):
    monthly = e1 + e2 + e3 + e4 + e5 + e6
    return monthly

# The nested function still needs to have the required arguments otherwise
# what values would it be using when the function is called.
def annual_costs():
    annual = monthly_costs(e1, e2, e3, e4, e5, e6) * 12
    return annual

print("Your monthly costs are",monthly_costs(e1, e2, e3, e4, e5, e6),"and you annual costs are",annual_costs())

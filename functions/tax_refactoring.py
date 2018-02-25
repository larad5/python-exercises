# 2.Sales Tax Program Refactoring

purchase = float(input("What is the amount of the purchase? "))

def state_Tax(s):
    stateTax = .05 * s
    print("The state tax for your purchase is", format(stateTax, '.2f'))
    return stateTax

def county_Tax(c):
    countyTax = .025 * c
    print("The county tax for your purchase is", format(countyTax, '.2f'))
    return countyTax

totalPurchase = purchase + state_Tax(purchase) + county_Tax(purchase)
print(format(totalPurchase, '.2f'))

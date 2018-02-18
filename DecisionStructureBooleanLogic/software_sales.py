# 12. Software Sales

#ask the user how many packages they want to purchased
pack = int(input("How many packages would you like to purchase? "))

#calculate the amount of discount depending on the amount of number purchased.
if pack < 10:
    print("There is no discount")
    discount = 0
elif pack <20:
    print("You get a 10% discount")
    discount = .10
elif pack <50:
    print("You get a 20% discount")
    discount = .20
elif pack < 100:
    print("You get a 30% discount")
    discount = .30
else:
    print("You get a 40% discount")
    discount = .40

price = 99
subTotal = price * pack
cost = subTotal - (subTotal * discount)

print("Your cost after discount will be", cost, "from the original price of", subTotal)

# 13. Shipping Charges

# ask the user for the weight of the package
weight = float(input("Enter the weight of your package: "))

# determine the shipping rate based on the weight of the package
# decision structure with boolean operators in the condition
if weight < 2 :
    rate = 1.50
elif weight > 2 and weight <= 6 :
    rate = 3.00
elif weight > 6 and weight <= 10 :
    rate = 4.00
elif weight > 10 :
    rate = 4.75

# calculate the shipping cost
shipping = weight * rate


# display shipping charges to the user
print("Based on the weight entered, your shipping cost will be $", format(shipping, '.2f'), sep='')

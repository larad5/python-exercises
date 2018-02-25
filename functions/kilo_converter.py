# 1. Kilometer Converter

# value-returning function with argument
def converter(kilo):
    # the variable miles is a local variable
    # the scope of the variable is limited to this function
    miles = kilo * 0.6214
    return miles

kilo = int(input("Enter a distance in kilometers: "))
print(converter(kilo))

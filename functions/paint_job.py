# 8.Paint Job Estimator

# User input for square feet of wall to paint
sqftWall = int(input("Enter the square footage of wall space to be painted: "))
galPrice = float(input("Enter the cost of the paint per gallon: "))
# Main function to process all information.
def main(sqftWall,galPrice):
    print("Gallons:",calc_gallons(sqftWall))
    print("Hours of labor:",calc_laborHours(sqftWall))
    print("Cost of paint: $",format(calc_paintCost(galPrice,sqftWall),'.2f'),sep='')
    print("Labor charges: $",format(calc_laborCharges(sqftWall),'.2f'),sep='')
    print("\nThe total cost of the paint job is $",format(calc_totalCost(sqftWall,galPrice),'.2f'),sep='')

# Calculate the number of whole gallons needed to paint.
def calc_gallons(sqftWall):
    gallons = (sqftWall / 112)
    return gallons

# Calculate the hours of labor requires for the square footage.
def calc_laborHours(sqftWall):
    laborHours = (sqftWall / 112) * 8
    return laborHours

# Calculate the cost of the paint needed to complete the job.
def calc_paintCost(galPrice,sqftWall):
    paintCost = galPrice * calc_gallons(sqftWall)
    return paintCost

def calc_laborCharges(sqftWall):
    laborCharges = 35 * calc_laborHours(sqftWall)
    return laborCharges

def calc_totalCost(sqftWall,galPrice):
    totalCost = calc_paintCost(galPrice,sqftWall) + calc_laborCharges(sqftWall)
    return totalCost

main(sqftWall,galPrice)

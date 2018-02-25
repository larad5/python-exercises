# 9.Monthly Sales Tax

totalSales = float(input("Enter the tota sales for the month: "))

def main(totalSales):
    print("The total sales tax is $",format(total_salesTax(totalSales),'.2f'),sep='')

def county_salesTax(totalSales):
    salesTax = .025 * totalSales
    return salesTax

def state_salesTax(totalSales):
    salesTax = .05 * totalSales
    return salesTax

def total_salesTax(totalSales):
    totalTax = county_salesTax(totalSales) + state_salesTax(totalSales)
    return totalTax

main(totalSales)

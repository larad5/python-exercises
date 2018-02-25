# 5. Property Tax

actual = float(input("What is the property's actual value? "))

def assessment_calculator(x):
    assess = x * .60
    print("The assessment value of the property is $",format(assess,'.2f'),sep='')
    return assess

def tax_calculator(x):
    tax = (assessment_calculator(x) // 100)*.72
    print("The property tax is $",format(tax,'.2f'),sep='')
    return tax

tax_calculator(actual)

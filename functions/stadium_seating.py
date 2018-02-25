# 7.Stadium Seating

clA = int(input("Class A tickets sold: "))
clB = int(input("Class B tickets sold: "))
clC = int(input("Class C tickets sold: "))

def main(a, b, c):
    income = A(a) + B(b) + C(c)
    print("The total ticket income was $",income,sep='')

def A(a):
    revenue = a * 20
    return revenue

def B(b):
    revenue = b * 15
    return revenue

def C(c):
    revenue = c * 10
    return revenue

main(clA, clB, clC)

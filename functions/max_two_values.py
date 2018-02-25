# 12. Maximum of Two Values

# functions
def maximum(a,b):
    if a > b :
        return a #the value that is returned can be within a decision structure
    else:
        return b

# program
num1 = int(input("First number: "))
num2 = int(input("Second number: "))

print("The greater number is",maximum(num1,num2))

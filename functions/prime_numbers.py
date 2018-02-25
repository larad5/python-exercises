 # Imports

 # Functions
def is_prime(num):
    if num < 2:
        status = False
    elif num == 2:
        status = True
    else:
        for x in range(2, num):
            test = num % x
            if (test == 0):
                status = False #not prime
                break
            else:
                status = True #prime
    return status
 # Program
num = int(input("Enter a number: "))
print("Is it prime? ",is_prime(num))

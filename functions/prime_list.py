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

for x in range(0,101):
    print(x,"\t",is_prime(x))

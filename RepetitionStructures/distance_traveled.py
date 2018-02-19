# 4. Distance Traveled

# ask the user for the speed of the vehicle and number of hours traveled
speed = int(input("Enter speed: "))
hours = int(input("Enter hours traveled: "))

# repetition structre to print out the distance traveled for each hour
for x in range(1, hours + 1):
    dist = speed * x
    if x == 1 :
        print("Hour\tDistance Traveled\n-----------------------------")
    print(x,"\t", dist,sep='')

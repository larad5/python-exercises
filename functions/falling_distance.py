# 13.Falling Distance

# imports
# functions
def falling_distance(t):
    g = 9.8
    distance = (1/2)*g*(t**2)
    return distance

# program
print("Time\t\t Distance Fallen")
for x in range(1,11):
    print(x,"second(s)\t",falling_distance(x),"meters")

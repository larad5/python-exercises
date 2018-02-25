# 10.Feet to Inches

feet = int(input("Enter the number of feet you want converted to inches: "))

def feet_to_inches(feet):
    inches = feet * 12
    return inches

print("There are",feet_to_inches(feet),"inches in",feet,"feet.")

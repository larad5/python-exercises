# 14. Body Mass Index

# ask user to enter their body weight
weight = float(input("Please enter your weight in terms of pounds: "))

# ask user to enter their height
height = float(input("Please enter your height in terms of inches: "))

# determine the user's BMI
bmi = weight * (703/(height**2))

# detemine their weight status
if bmi < 18.5 :
    status = "Underweight"
elif bmi >= 18.5 and bmi <= 25 :
    status = "optimal weight"
else:
    status = "Overweight"

# display the user's weight status/BMI
print("Your current BMI is", int(bmi), "and health status is", status)

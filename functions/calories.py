# 6.Calories from Fat and Carbohydrates

fatConsumed = int(input("Grams of fat consumed: "))
carbConsumed = int(input("Grams of carbs consumed: "))

def main(a, b):
    calories_fat(a)
    calories_carb(b)

def calories_fat(a):
    fatCals = a * 9
    print("Calories from fat:",fatCals)

def calories_carb(a):
    carbCals = a * 4
    print("Calories from carbs:",carbCals)

main(fatConsumed, carbConsumed)

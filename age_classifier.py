age = int(input("Enter a person's age: "))

if age <= 1:
    print("infant")
if age > 1 and age <13:
    print("child")
if age >= 13 and age <20:
    print("teenager")
if age >= 20:
    print("adult")

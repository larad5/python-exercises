l1 = int(input("What is the first rectangle's length? "))
w1 = int(input("What is the first rectangle's width? "))

l2 = int(input("What is the second rectangle's length? "))
w2 = int(input("What is the second rectangle's width? "))

a1 = l1 * w1
a2 = l2 * w2

if a1 > a2:
    print("The area of the first rectangle is greater of the two.")
elif a1 < a2:
    print("The area of the second rectangle is greater of the two.")
else:
    print("The area of both rectangles is the same!")

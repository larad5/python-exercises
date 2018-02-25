# 15.Test Average and Grade

# Imports

# Functions
def calc_average(t1,t2,t3,t4,t5):
    average = (t1+t2+t3+t4+t5)/5
    return average

def determine_grade(score):
    if score < 40 :
        grade = "F"
    elif score < 69 :
        grade = "D"
    elif score < 79 :
        grade = "C"
    elif score < 89 :
        grade = "B"
    else:
        grade = "A"
    return grade


# Program
t1 = int(input("Enter test 1 score:"))
t2 = int(input("Enter test 2 score:"))
t3 = int(input("Enter test 3 score:"))
t4 = int(input("Enter test 4 score:"))
t5 = int(input("Enter test 5 score:"))

calc_average(t1,t2,t3,t4,t5)

print("Score\t Grade")
print(t1,"\t",determine_grade(t1))
print(t2,"\t",determine_grade(t2))
print(t3,"\t",determine_grade(t3))
print(t4,"\t",determine_grade(t4))
print(t5,"\t",determine_grade(t5))
print("\nTest Average:",calc_average(t1,t2,t3,t4,t5))

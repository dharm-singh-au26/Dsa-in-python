"""
A school has following rules for grading system:
a. Below 25 - F
b. 25 to 45 - E
c. 45 to 50 - D
d. 50 to 60 - C
e. 60 to 80 - B
f. Above 80 - A
Ask user to enter marks and print the corresponding grade.
"""
marks = int(input("Enter your marks : "))

if marks > 80 :
    print("Your Grade is : A ")
elif (80 >= marks > 60) :
    print("Your Grade is : B ")
elif 60 >= marks > 50 :
    print("Your Grade is : C ")
elif 50 >= marks > 45 :
    print("Your Grade is : D ")
elif 45 >= marks > 25 :
    print("Your Grade is : E ")
else:
    print("Your Grade is : F ")
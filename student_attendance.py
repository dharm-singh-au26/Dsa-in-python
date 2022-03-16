"""
A student will not be allowed to sit in exam if his/her attendence is less than 75%.
Take following input from user
Number of classes held
Number of classes attended.
And print
percentage of class attended
Is student is allowed to sit in exam or not.
"""
number_of_classes_held = int(input("Enter here Number of classes held : "))
Number_of_classes_attended = int(input("Enter here Number of classes attended :"))

attendance = (Number_of_classes_attended/number_of_classes_held)*100
print(f"your attendance is : {attendance}")

if attendance < 75 :
    print("Sorry! you are not allow to sit in exam")
else:
    print("Congratulation, You are Allow to sit in exam")

"""
Modify the above question to allow student to sit if he/she has medical cause. Ask user if he/she has medical cause or not ( 'Y' or 'N' ) and print accordingly.
"""
number_of_classes_held = int(input("Enter here Number of classes held : "))
Number_of_classes_attended = int(input("Enter here Number of classes attended :"))
medical_cause = input("enter your medical cause Yes or Not ")


attendance = (Number_of_classes_attended/number_of_classes_held)*100
print(f"your attendance is : {attendance}")

if attendance < 75 :
    if medical_cause == "Yes":
        print("Congratulation, You are Allow to sit in exam")
    else:
        print("Sorry! you are not allow to sit in exam")


else:
    print("Congratulation, You are Allow to sit in exam")
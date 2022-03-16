"""
Ask user to enter age, sex ( M or F ), marital status ( Y or N ) and then using following rules print their place of service.
if employee is female, then she will work only in urban areas.

if employee is a male and age is in between 20 to 40 then he may work in anywhere

if employee is male and age is in between 40 t0 60 then he will work in urban areas only.

And any other input of age should print "ERROR"
"""
age = int(input("Enter age here :"))
sex = input("Enter sex here (M or F) : ")
# marital_status = input("Enter maritalstatus (Y or N)")

if sex == "F":
    print("she will work only in urban areas")
elif sex=="M" and 40 > age > 20 :
    print("he may work anywhere")
elif sex == "M" and 60 > age >= 40 :
    print("he will work in urban areas only")
else:
    print("ERROR")
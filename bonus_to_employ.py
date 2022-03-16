"""
A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years.
Ask user for their salary and year of service and print the net bonus amount.
"""

year = int(input("enter the years of service in company :"))
salary = int(input("Enter your salary : "))

if year > 5 :
    bonus = (salary*5)/100
    print(f"your bonus is : {bonus}")
else:
    print("you are not eligile for bonus .")
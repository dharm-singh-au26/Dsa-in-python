"""
A shop will give discount of 10% if the cost of purchased quantity is more than 1000.
Ask user for quantity
Suppose, one unit will cost 100.
Judge and print total cost for user.
"""

quantity = int(input("Enter Quatity here :"))

cost = quantity*100

if cost > 1000 :
    price_to_pay = cost - ((cost*10)/100)
    print("After discont price be :", price_to_pay)
else:
    print("Not eligible for discount pay ammount :", cost)
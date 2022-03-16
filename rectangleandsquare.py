"""
Take values of length and breadth of a rectangle from user and check if it is square or not.
"""

length = int(input("Enter the length :"))
breadth = int(input("Enter the breadth :"))

if length == breadth:
    print("it is a square.")
else:
    print("it is a rectangle.")
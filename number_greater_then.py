"""
Take two number and check whether the sum is greater than 5, less than 5 or equal to 5.
"""

num1 = int(input("Enter number 1 : "))
num2 = int(input("Enter number 2 : "))

sum = num1+num2

if sum > 5:
    print("sum is greater than 5 and sum is :",sum)
elif sum < 5:
    print("sum is less than 5 and sum is :",sum)
else:
    print("sum is equal to  5 and sum is :",sum)
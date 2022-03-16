"""
Calculate the sum of digits of a number given by user. E.g.-
INUPT : 123        OUPUT : 6
INUPT : 12345        OUPUT : 15
"""

n = int(input("Enter the digit : "))

sum = 0 
while n > 0 :
    a = n % 10 
    sum = sum+a
    n = n//10

print(sum)
"""
A three digit number is called Armstrong number if sum of cube of its digit is equal to number itself.
E.g.- 153 is an Armstrong number because (1^3)+(5^3)+(3^3) = 153.
Write all Armstrong numbers between 100 to 500.
"""
num = int(input("Enter the digit : "))

sum = 0 
temp = num
while temp > 0 :
    digit = temp % 10 
    sum += digit**3
    temp //= 10

if sum == num:
    print(num,": is armstrong number ")
else:
    print(num,":is not armstrong number ")

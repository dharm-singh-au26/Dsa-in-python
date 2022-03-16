"""
Write a program to find greatest common divisor (GCD) or highest common factor (HCF) of given two numbers.
"""
num1 = int(input("Enter First number :"))
num2 = int(input("Enter Second number :"))

def HCF(x,y):
    if x>y:
        smaller = y
    else:
        smaller = x
    
    for i in range (1,smaller+1):
        if((x%i==0)and(y%i==0)):
            hcf = i
    return hcf

print("HCF Is :",HCF(num1,num2))

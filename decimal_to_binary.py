"""
Given a decimal Number , Write a program to convert Decimal to Binary
number.
Input : 10 (decimal)
Output: - 1010
Explanation:
As, discussed in class , We can do %2 and //2 approach till the number is
positive and store the remainder and then reverse the same.
Sample :
def Decimal_to_Binary(number):
"""

def Decimal_to_Binary(number):
    if number >= 1:
        Decimal_to_Binary(number//2)
    print(number%2 , end = " ")


Decimal_to_Binary(10)
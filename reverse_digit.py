"""
A 4 digit number is entered through keyboard. Write a program to print a new number with digits reversed as of orignal one. E.g.-
INPUT : 1234        OUTPUT : 4321
INPUT : 5982        OUTPUT : 2895
"""

n = int(input("Enter digit here : "))

rev = 0

while(n > 0):
	a = n % 10
	rev = rev * 10 + a
	n = n // 10

print(rev)



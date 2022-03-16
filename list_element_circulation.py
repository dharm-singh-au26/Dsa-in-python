"""

2.Write a program to shift every element of a list to circularly right. E.g.-
INPUT : 1 2 3 4 5
OUTPUT : 5 1 2 3 4
"""
a = [1,2,3,4,5]
b = [a[len(a)-1]]+a[:len(a)-1]
print (b)
# a = b
# print (a)
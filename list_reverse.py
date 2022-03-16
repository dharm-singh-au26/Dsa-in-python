"""
Take 10 integer inputs from user and store them in a list. Now, copy all the elements in another list but in reverse order.
"""

i = 0
a = []
while i<10:
        
    num = int(input("Enter number"))
    a.append(num)
    i = i+1
print(a)
a.reverse()
b=a
print(b)
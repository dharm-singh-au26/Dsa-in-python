"""
Take 10 integer inputs from user and store them in a list and print them on screen.
"""
#  using for loop :
list1 = []

for i in range(1,11):
    num = int(input("enter number here :"))
    list1.append(num)

print (list1)

# using while loop :
list2 = []
i = 1
while i<11 :
    num = int(input("enter number here :"))
    list2.append(num)
    i = i+1
print(list2)

# -------------OUTPUT--------
"""
enter number here :5
enter number here :2
enter number here :3
enter number here :4
enter number here :8
enter number here :7
enter number here :5
enter number here :6
enter number here :2
enter number here :1
[5, 2, 3, 4, 8, 7, 5, 6, 2, 1]
"""


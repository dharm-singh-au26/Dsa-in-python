"""
Take 10 integer inputs from user and store them in a list. Again ask user to give a number. Now, tell user whether that number is present in list or not.
( Iterate over list using while loop ).
"""
list1 = []

for i in range(1,11):
    num = int(input("enter number here :"))
    list1.append(num)

print(list1)

number  = int(input("enter number here :"))

if number in list1:
    print("Yes")
else: 
    print("NO")
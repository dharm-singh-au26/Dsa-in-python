"""
Take 10 integers from keyboard using loop and print their average value on the screen.
"""


# sum = 0

# i = 10
# while i>0:
#   print ("Enter number")
#   num = int(input())
#   sum = sum + num
#   i = i-1
# print ("average is",sum/10.0)

i = 1
sum = 0
while i < 11 :
    num = int(input("Enter number here : "))
    sum = sum + num 
    i += 1
print("average is :",sum/10)
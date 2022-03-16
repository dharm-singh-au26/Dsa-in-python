# MAP FUNCTION 
# WE CAN USE MAP FUNCTION CONVERT STRING TO INTEGER OR ADD LIST 

lis = ["64","35","62","15"]
# using for loop
for idx in range(len(lis)):
    lis[idx] = int(lis[idx])

lis[2] = lis[2] + 3
print(lis[2])

# above same function we can done using map function :
lis = ["64","35","62","15"]
lis = list(map(int,lis))
lis[2] = lis[2] + 3
print(lis[2])

# square of list using map function :

number = [5,8,9,4,12,258,874]

square = list(map(lambda x : x*x, number))
print(square)
# ////////////////////////////////////////////////////////////////
# Filter Function 

lis = [1,2,3,4,5,6,7,8,9,10]
def is_greater_5(num):
    return num > 5

gr_then_5 = list(filter(is_greater_5,lis))

print(gr_then_5)

# ---------------------REDUCE FUNCTION--------------------------

from functools import reduce

lis = [1,2,3,4,5]
num = reduce(lambda x,y : x*y, lis)
print(num)
"""
Take integer inputs from user until he/she presses q ( Ask to press q to quit after every integer input ). Print average and product of all numbers.
"""
raw_input = input("Enter q to quit or any other key to continue")
summ = 0
count = 1
while( raw_input != 'q'):
    temp = input()
    if(temp == 'q'):
      break
    summ = summ+int(temp)
    count=count+1
  
  
print (summ/(count*1.0))



# n = input()
# user_input = []
# avg = 0
# a = 0
# for i in range (int(n)):
#     if (n=="q"):
#         print("terminated successfully")
#         break
#     else:
#         user_input = int(input("Enter number here :"))
#         avg += user_input[i]
#         a = avg/n
#     print(a)

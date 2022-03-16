"""
Write a function to return sum of rows of a matrix as a list: (5 marks)
"""




x = 100
M = []


R = int(input("Enter row for the matrix : "))
C= int(input("Enter col for the matrix : "))
for i in range(R) :
        for j in range(C) :
            M[i][j] = int(input("enter value").split( ))
 
        x += 1


# for i in range (R):
#     A = []
#     for j in range (C):
#         A.append(int(input("enter elements")))
#     M.append(A)

# for i in range (R):
#     for j in range (C):
#         print(M[i][j],end=" ")
#     print()

#  sum of rows :
sumOfRow= 0 
sumOfColumn =0
list1 = []
list2 =[]


for i in range (R):
    for j in range(C):
        # if i == 0:

        sumOfRow = sumOfRow + M[i][j]
        sumOfColumn += M[j][i]
    # print("sum of" , i ,"row  = ", sum)
    list1.append(sumOfRow)
    list2.append(sumOfColumn)
    sumOfRow = 0
    sumOfColumn = 0
print(list1)
print(list2)

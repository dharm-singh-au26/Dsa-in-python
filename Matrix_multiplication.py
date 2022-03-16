p = int(input("Enter the number of rows :"))
q = int(input("Enter the number of col :"))
n = int(input("Enter the number of col for matrix1 and number of rows for matrix2 :"))
Matrix1 = []

for i in range(p):
    a= []
    for j in range(n):
        a.append(int(input()))
    Matrix1.append(a)

for i in range (p):
    for j in range(n):
        print((Matrix1[i][j]),end = " ")
    print()

# # matrix 2
# p = int(input("Enter the number of rows :"))
# q = int(input("Enter the number of col :"))
# n = int(input("Enter the number of col for matrix1 and number of rows for matrix2 :"))
Matrix2 = []

for i in range(n):
    a= []
    for j in range(q):
        a.append(int(input()))
    Matrix1.append(a)

for i in range (n):
    for j in range(q):
        print((Matrix1[i][j]),end = " ")
    print()



result = [[0 for i in  range(p)] for j in range(q) ]


for i in range(p):
    for j in range(q):
        for k in range (n):

            result[i][j] = Matrix1[i][j]  +  Matrix1[i][k] *  Matrix2[k][j]


print("result of matrix1 + matrix2 is :")
    
for i in range (p):
    for j in range(q):
        print((result[i][j]),end = " ")
    print()
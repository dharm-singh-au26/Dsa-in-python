row = int(input("Enter the number of rows :"))
col = int(input("Enter the number of col :"))
Matrix1 = []

for i in range(row):
    a= []
    for j in range(col):
        a.append(int(input()))
    Matrix1.append(a)

for i in range (row):
    for j in range(col):
        print((Matrix1[i][j]),end = " ")
    print()

# matrix 2
row = int(input("Enter the number of rows :"))
col = int(input("Enter the number of col :"))
Matrix2 = []

for i in range(row):
    a= []
    for j in range(col):
        a.append(int(input()))
    Matrix2.append(a)
for i in range (row):
    for j in range(col):
        print((Matrix2[i][j]),end = " ")
    print()


result = [[0 for i in  range(col)] for j in range(row) ]


for i in range(row):
    for j in range(col):
        result[i][j] = Matrix1[i][j]  +  Matrix2[i][j]


print("result of matrix1 + matrix2 is :")
    
for i in range (row):
    for j in range(col):
        print((result[i][j]),end = " ")
    print()
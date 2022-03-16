row = int(input("Enter the number of rows :"))
col = int(input("Enter the number of col :"))
Matrix = []

for i in range(row):
    a= []
    for j in range(col):
        a.append(int(input()))
    Matrix.append(a)


for i in range (row):
    for j in range(col):
        print(format(Matrix[i][j]),end = " ")
    print()
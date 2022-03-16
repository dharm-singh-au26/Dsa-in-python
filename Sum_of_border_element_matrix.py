'''
Q - 2) Write a program to print sum of border elements of a square Matrix.
'''
R = int(input("Enter row for the matrix : "))
C= int(input("Enter col for the matrix : "))
M = []

for i in range (R):
    A = []
    for j in range (C):
        A.append(int(input("enter elements")))
    M.append(A)

for i in range (R):
    for j in range (C):
        print(M[i][j],end=" ")
    print()

sum = 0
for i in range (R):
    for j in range (C):
        if i== 0 or i == R-1 or j==0 or j==C-1 :
            sum += M[i][j]


print(sum)



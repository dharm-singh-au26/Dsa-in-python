'''
Q - 1) Write a program to print sum of right diagonal of a matrix: (5 marks)
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

# sum of right diagonal 

def sum_right_diagonal(M):
    sum = 0
    for i in range (R):
        sum += M[i][R-1-i]
    return sum
print(sum_right_diagonal(M))
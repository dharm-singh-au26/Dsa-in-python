'''
4 3
0 1 2
3 0 1
4 3 0
5 4 3
'''
# row = int(input("Enter the number of rows :"))
# col = int(input("Enter the number of col :"))
# Matrix1 = []

# for i in range(row):
#     a= []
#     for j in range(col):
#         a.append(int(input()))
#     Matrix1.append(a)

# for i in range (row):
#     for j in range(col):
#         print((Matrix1[i][j]),end = " ")
#     print()

# a = Matrix1[0][0]
# print(a)
# for i in range(row):
#     if a == Matrix1[i][i]:
#         print("yes")
#         break
#     else:
#         print("no")
#         break

n, m = [int(x) for x in input().split()]
matrix = []
for i in range(n):
    a = list(map(int, input().split()))
    matrix.append(a)
b = []
for i in range(n):
    for j in range(m):
        if i == j:
            b.append(matrix[i][j])

print(b)
count = 0
for i in range(len(b) - 1):
    if b[i] != b[i + 1]:
        count += 1
if count == 0:
    print("YES")
else:
    print("NO")
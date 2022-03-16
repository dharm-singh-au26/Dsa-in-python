"""
Question : 2 -
Given a number , find if the number is a perfect square root or not ? --- Marks :-5
Also , find Time and space Complexity
example :
Input : n = 4
output : - True
Input : n = 10
output : - False
Explanation : since square root (4) =2 (perfect square ) --true
Square root(10) = 3.35 (Not perfect square) -- false
Sample :
Def find_perfect_square(N):
"""


from math import sqrt
def square_root(n):
   sq_root = int(sqrt(n))
   return (sq_root*sq_root) == n
n = int(input("enter number here :"))
print (square_root(n))

#  TIME-COMPLEXITY === O(n)
#  SPACE-COMPLEXITY ==== O(n)
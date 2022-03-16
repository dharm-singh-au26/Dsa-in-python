"""
Write a Program to swap values , without using 3rd variable .
Also find Time and Space Complexity --- Marks : - 5
Example : -
Input : -
A = 20 , B = 10
Output : - A = 10 , B = 20
Explanation : - values has been swapped
Sample :
Def swap(A,B):

"""
A = int(input("enter value of A:"))
B = int(input("enter value of B :"))

A,B = B,A
print("value of A is ",A)
print("value of B is ",B)

# TIME-COMPLEXITY====O(1)
# SPACE-COMPLEXITY====O(1)
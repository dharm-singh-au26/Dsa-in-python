"""
Given a sorted array with Duplicates . Write a program to find UPPER
BOUND of a TARGET using Binary search Method .
Return Index corresponding to the element of the upper bound element.
Example :
Input : - arr = [1,1,1,2,2,3,3,5,5,5,7,7] , Target = 4
Output : - 7
"""
arr = [1,1,1,2,2,3,3,5,5,5,7,7]
target = 4

def Upper_Bound(arr , target):
    n = len(arr)
    left = 0 
    right = n - 1
    a = 0 
    c = 0

    while (left <= right) :
        mid = (left+right)//2
        if arr[mid] == target:
            a = mid 
            c = 1 
            left = mid + 1
        elif arr[mid] > target:
            right = mid - 1 
        else:
            left = mid + 1
    if c == 0:
        return mid 
    else:
        return a
        
print(Upper_Bound(arr , target))


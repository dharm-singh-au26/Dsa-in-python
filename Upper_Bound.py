"""
Given an sorted integer array . Write a program to find UPPER Bound of
target number , return the index of the element .
Input : - arr = [1,2,2,2,3,3,5,5,5,6,6,7,7] , target = 7
Output: - 12
"""

A = [1,2,2,2,3,3,5,5,5,6,6,7,7]
target = 7
def upperBound(A, target):
    n = len(A)
    left = 0
    right = n - 1
    ans = -1
    while left <= right:
        mid = (left + right)>>1
        if A[mid] == target:
            ans = mid
            left = mid + 1
        elif A[mid] > target:
            right = mid - 1
        elif A[mid] < target:
            left = mid + 1
    return ans
print(upperBound(A, target))
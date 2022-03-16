'''
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.

 

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Explanation: [4,9] is also accepted.
'''

def intersection_of_array(A1,A2):
    intersection = []
    for i in A1:
        if i in A2:
            if i not in intersection:
                intersection.append(i)
    return intersection

A1 = [1,2,3,4,5,8,7,6,9]
A2 = [9,4,6,2,6,8,6,8,6,2]

print(intersection_of_array(A1,A2))

# https://leetcode.com/problems/intersection-of-two-arrays/submissions/s

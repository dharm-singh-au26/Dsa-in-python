'''
Q-1 )Find the Duplicate Number:
https://leetcode.com/problems/find-the-duplicate-number/
(Solve the above using both the approaches discussed in class) and comment on
time
complexity.
:(5 marks)
Given an array of integers nums containing n + 1 integers where each integer is
in the range [1, n] inclusive.
There is only one repeated number in nums, return this repeated number.
You must solve the problem without modifying the array nums and uses only
constant extra space.
Example 1:
Input: nums = [1,3,4,2,2]
Output: 2

'''
nums = [1,3,4,2,2]

def dup(nums):
    ht = dict()
    N = len(nums)
    for i in nums:
        if i not in ht :
            ht[i] = 1
        else:
            ht[i] += 1
    
    for key,value in ht.items():
        if value == 2:
            duplicate = key
            break

    return duplicate

a = dup(nums)
print(a)
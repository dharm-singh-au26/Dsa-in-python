'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

https://leetcode.com/problems/two-sum/
 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].
'''
nums = [2,7,2,15]
target = 9

def two_sum(nums,target):
    for i in range (len(nums)):
        for j in range (i+1,len(nums)):
            sum = nums[i] + nums[j]
            if sum == target:
                return [i,j]

            
a = two_sum(nums,target)
print(a)
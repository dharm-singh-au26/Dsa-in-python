'''
Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [1,3,6,10]
Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].
'''
nums = [1,2,3,4]
def running_sum(nums):
    # new_nums = [nums[0]]
    # for i in range(1, len(nums)):
    #     new_nums.append(nums[i] + new_nums[i-1])
    # return new_nums
    sum = 0 
    a = []
    for i in range (0,len(nums)):
        sum = sum + nums[i]
        a.append(sum)
    return a
print(running_sum(nums))
'''
Q-2 )Sum of Unique Elements:
https://leetcode.com/problems/sum-of-unique-elements/
(5 marks)
You are given an integer array nums. The unique elements of an array are the elements that appear
exactly once in the array.
Return the sum of all the unique elements of nums.
Example 1:
Input: nums = [1,2,3,2]
Output: 4
'''
nums = [1,2,3,4,4,5]
def unique_element(nums):
    res = dict()

    for i in nums:
        if i in res :
            res[i] = res[i] + 1
        else:
            res[i] = 1
    count = 0
    for i in res :
        if res[i] == 1:
            count = count + i
    return count
print(unique_element(nums))

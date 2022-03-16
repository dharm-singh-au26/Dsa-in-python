"""
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

 

Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
Example 2:

Input: nums = [0,1]
Output: [[0,1],[1,0]]
Example 3:

Input: nums = [1]
Output: [[1]]
 

Constraints:

1 <= nums.length <= 6
-10 <= nums[i] <= 10
All the integers of nums are unique.
"""

# Python function to print permutations of a given list
# def permutation(lst):

# 	# If lst is empty then there are no permutations
# 	if len(lst) == 0:
# 		return []

# 	# If there is only one element in lst then, only
# 	# one permutation is possible
# 	if len(lst) == 1:
# 		return [lst]

# 	# Find the permutations for lst if there are
# 	# more than 1 characters

# 	l = [] # empty list that will store current permutation

# 	# Iterate the input(lst) and calculate the permutation
# 	for i in range(len(lst)):
# 	    m = lst[i]

# 	# Extract lst[i] or m from the list. remLst is
# 	# remaining list
# 	remLst = lst[:i] + lst[i+1:]

# 	# Generating all permutations where m is first
# 	# element
# 	for p in permutation(remLst):
# 		l.append([m] + p)
# 	return l


# # Driver program to test above function
# data = list('01')
# for p in permutation(data):
# 	print (p)

def permute(LIST):
    length=len(LIST)
    if length <= 1:
        yield LIST
    else:
        for n in range(0,length):
             for end in permute( LIST[:n] + LIST[n+1:] ):
                 yield [ LIST[n] ] + end

for x in permute([1,0]):
    print(x)
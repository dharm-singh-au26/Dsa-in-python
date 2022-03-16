"""
Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

 

Example 1:

Input: x = 2.00000, n = 10
Output: 1024.00000
Example 2:

Input: x = 2.10000, n = 3
Output: 9.26100
Example 3:

Input: x = 2.00000, n = -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25
 

Constraints:

-100.0 < x < 100.0
-231 <= n <= 231-1
-104 <= xn <= 104

"""

# Python3 code for extended version
# of power function that can work
# for float x and negative y

# def power(x, y):

# 	if(y == 0): return 1
# 	temp = power(x, int(y / 2))
	
# 	if (y % 2 == 0):
# 		return temp * temp
# 	else:
# 		if(y > 0): return x * temp * temp
# 		else: return (temp * temp) / x
	
# # Driver Code
# x = int(input("enter the number :"))
# y = int(input("enter the power :"))
# print('%.6f' %(power(x, y)))


# "anagram means how much meaningful words can be generated from rotatiing their postions
# for ex.- eat-------- eat,ate,tea and tan---tan,nat and uning bat--- only bat is generated
# "

# i hope you understood. if not then feel free to ping me at 9462686862

# This code is contributed by Smitha Dinesh Semwal.

# Function to group anagrams from a given list of words
def groupAnagrams(strs):
    # a list to store anagrams
    anagrams = []
 
    # base case
    if not strs:
        return anagrams
 
    # sort each word on the list
    nums = [''.join(sorted(word)) for word in strs]
 
    # construct a dictionary where the key is each sorted word,
    # and value is a list of indices where it is present
    d = {}
    for i, e in enumerate(nums):
        d.setdefault(e, []).append(i)
 
    # traverse the dictionary and read indices for each sorted key.
    # The anagrams are present in the actual list at those indices
    for index in d.values():
        collection = tuple(strs[i] for i in index)
        if len(collection) > 1:
            anagrams.append(collection)
 
    return anagrams
 
 
if __name__ == '__main__':
    # a list of strs
    strs = ["eat","tea","tan","ate","nat","bat"]
 
    anagrams = groupAnagrams(strs)
    for anagram in anagrams:
        print(anagram)
 
'''
Q - 2 ) https://leetcode.com/problems/plus-one/
Given a non-empty array of decimal digits representing a non-negative integer, increment one
to the integer.
The digits are stored such that the most significant digit is at the head of the list, and each
element in the array contains a single digit.
You may assume the integer does not contain any leading zero, except the number 0 itself.
Example 1:
Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
'''

digits = [1,2,3]
def plusOne(self,digits):
    if len(digits) == 0:
        return(1)
    if digits[-1] != 9:
        digits[-1] += 1
        return(digits)
    else:
        digits = self.plusOne(digits[:-1])
        digits.append(0)
        return digits

print(plusOne(digits))
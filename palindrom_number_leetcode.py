'''
Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward. For example, 121 is palindrome while 123 is not.

 

Example 1:

Input: x = 121
Output: true
'''

x = 121
def palindrom(x):
    if x < 0 :
        return False
    
    c = x 
    b = 0 
    while c :
        b = b*10 + c %10
        c = c // 10

    return b == x
print(palindrom(x))
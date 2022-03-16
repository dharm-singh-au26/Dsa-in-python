"""
Given an integer array , every element is repeated TWICE , except one
element , Find that element ?
Input : - [1 , 2 , 1, 2 ,4 , 3 ,4 ,3]
Output: - 3
Explanation : HINT : - Use XOR operator 
"""
arr = [5,5,1 , 2 , 1, 2 ,4 , 3 ,4]

temp = arr[0]
for i in range(1,len(arr)):
    temp = temp^arr[i]
    
print(temp)
"""
Q-2 ) Write a function that prints digits of a number from left to right , using
recursion:(5 marks)
Sample Input:
1234567
Sample output:
1
2
3
4
5
6
7
"""
def L_to_R (digit):
    if digit < 10:
        print (digit)
    else :
        L_to_R(digit//10)
    
        print(digit%10)

(L_to_R(12345))


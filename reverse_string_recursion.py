"""
If we have a string, write a function that prints reverse of that string, using
recursion.
Sample Input:
ABCD
Sample Output:
DCBA
"""
def reverse_string(string):
    if len(string)==0:
        return
    
    temp = string[0]
    reverse_string(string[1:])
    print(temp, end = "")

reverse_string("ABCD")
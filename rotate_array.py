"""
Given an array, rotate the array to the right by k steps, where k is non-negative.
"""

def right_rotate_array(a,n,k):

    k = k%n

    for i in range(0,n):
        if i<k :
            print(a[n+i-k],end = " ")
        else:
            print(a[i-k],end=" ")
    
    print("\n")

Array = [1,2,3,4,5]
N = len(Array)
K=4

right_rotate_array(Array,N,K)

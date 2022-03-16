"""
Given an array with NO Duplicates . Write a program to find PEAK
ELEMENT
Return value corresponding to the element of the peak element.
Example :
Input : - arr = [2,5,3,7,9,13,8]
Output : - 5 or 13 (anyone)
HINT : - Peak element is the element which is greater than both
neighhbours.
def FindPeak(arr ):
"""


arr = [2,5,3,7,9,13,8]
# arr = [13]
def Find_peak (arr) :
    n = len(arr)
    
    
    for i in range(0,n):
        if n==1 :
            return arr[i]

        if i==0 and arr[i] > arr[i+1]:
            return arr[i]

        elif (i == n-1  and arr[i]>arr[i-1]):
            return arr[i]

        elif (arr[i] > arr[i+1]) and (arr[i] > arr[i-1]):
            return arr[i]
            

print(Find_peak(arr))





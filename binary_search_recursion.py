"""
We have seen an iterative approach for binary search algorithm , write a
recursive approach for that.
HINT: when we divide the array into two parts, we need to perform a search on only one half.
Apply binary search only on that half.
"""

def binary_Search(arr,low,high,target):
    if high>=1:
        mid = (low + (high-1))//2
        
        if arr[mid] == target:
            return mid
        
        elif arr[mid] < target:
            return binary_Search(arr,mid+1,high,target)
        
        else:
            return binary_Search(arr,mid+1,high,target)
    
    else:
        return -1
    
arr = [1,2,5,8,9,10]
target = 8 
result = binary_Search(arr,0,len(arr)-1,target)
print(result)   
#  bubble sort :

arr = [5,4,3,2,1]

def bubble_sort(arr):
    n = len(arr)
    for i in range(0,n):
        for j in range(0,n-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
        print(*arr)
    return arr

a = bubble_sort(arr)
print(a)
def single_element(arr):
    op = arr[0]
    for i in range(1,len(arr)):
        op = op^arr[i]

    return op
arr = [1,2,1,3,2,4,5,8,4,5,8]
print(single_element(arr))


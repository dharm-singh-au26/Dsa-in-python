'''
Q - 4 ) (Objective of this question is to make you utilise memory(space
better)) (2 marks)
Reverse an array of integers and do not use inbuilt functions like “reverse”,
don’t use shorts hands like “arr[::-1]”. Only use following approach:
swap first and last element,
then second and second last element,
till middle

arr = [1,2,3,4,5,6]
rev_arr = [6,5,4,3,2,1]
'''
arr = [1,2,3,4,5,6]


start = 0
end = len(arr)-1

while start < end :
    arr[start] ,arr[end] = arr[end] ,arr[start]

    start += 1
    end -= 1
print(arr)





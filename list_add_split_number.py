"""
Take a list of length n where all the numbers are non-negative and unique. Find the element in the list possessing the highest value. Split the element into two parts where first part contains the next highest value in the list and second part hold the required additive entity to get the highest value. Print the list where the highest value get splitted into those two parts.
Sample input: 4 8 6 3 2
Sample output: 4 6 2 6 3 

"""
a = [4,8,6,3,2]
i = 0
largest = a[0]
while i<len(a):
    if largest<a[i]:
        largest = a[i]
        largest_index = i
    i = i+1
print(largest_index)

second_largest = a[0]
i = 0
while i < len(a):
    if largest != a[i] and second_largest < a[i]:
        second_largest = a[i]
    i = i+1
diffrence = (largest - second_largest)
print(a[:largest_index]+[second_largest,diffrence]+a[largest_index+1:])
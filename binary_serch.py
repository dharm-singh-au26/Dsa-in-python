list1 = []
n = int(input("element of list"))

for i in range(0,n):
    num = int(input("enter number here :"))
    list1.append(num)
    list1.sort()
print (list1)




def Binary_search(list1,key):
    low = 0
    high = len(list1)-1
    
    found = False
    while (low <= high) and (not found):
        mid = (low+high)//2
        if key == list1[mid]:
            found = True
        elif key > list1[mid]:
            low = mid + 1
        else:
            high = mid - 1
    if found == True:
        print("key is found")
    else:
        print("key is not found")
    
Binary_search(list1,5) 


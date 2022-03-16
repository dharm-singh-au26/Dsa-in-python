#  merge sort :

def mergesort(list1):
    if len(list1) > 1:
        mid = len(list1)//2
        left_list = list1[:mid]
        right_list = list1[mid:]
        mergesort(left_list)
        mergesort(right_list)
        i = 0 
        j = 0
        k = 0
        while len(left_list) > i and len(right_list) > j :
            if left_list[i] < right_list[j]:
                list1[k] = left_list[i]
                i = i+1
                k = k+1
            else:
                list1[k] = right_list[j]
                j = j+1
                k = k+1
        while i < len(left_list):
            list1[k] = left_list[i]
            i = i+1
            k = k+1
        while j < len(right_list):
            list1[k] = right_list[j]
            j = j+1
            k = k+1
        
    # return list1
list1 = [5,8,9,7,4,6,2,1,45,85,78,99]
# nums = int(input("how many element in list:"))
# list1 = [int(input()) for x in range (nums)]
mergesort(list1)


print(list1)


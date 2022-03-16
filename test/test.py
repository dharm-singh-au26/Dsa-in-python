"""
n = int(input())
while n > 9:
    n = sum(map(int, str(n)))
print(n)

"""
# n = int(input("Input an integer:"))

# def sum_digits(n):
#     newnum = 0
#     while n:
#         n, digit = divmod(n, 10)
#         newnum += digit
#     return newnum
# def getSum(n): 
     
#     sum = 0
#     while (n != 0): 
        
#         sum = sum + (n % 10)
#         n = n//10
        
#     return sum
    
# n = 12345
# print(getSum(n))

# while n > 9:
#     n = getSum(n)

# print(n)


def square_ele(list):
    a = sorted(list)
    res = []
    for i in range (0, len(a)):
        new_list = a[i] * a[i]
        res.append(new_list)
    res.sort()
    s = ' '.join(map(str, res))
    return s
n = int(input())
list = [int(x) for x in input().split()]
print(square_ele(list))
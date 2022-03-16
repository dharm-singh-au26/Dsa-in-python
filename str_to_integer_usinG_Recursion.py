

def myAtoi(string):
	res = 0

	for i in range(len(string)):
		res = res * 10 + (ord(string[i]) - ord('0'))

	return res
string = input("enter string here :")

print (myAtoi(string)+1)

# def myAtoi(string):
#     if (len(str) == 1):
#         return (ord(str[0]) - ord('0'))
#     else:
#         x = ord(str[0]) - ord('0')
#     	y = myAtoi(str[1:])
# 		x = x* 10 + (ord(len(str)) - ord('0'))
# 		return x



# string = input("enter string here :")

# print (myAtoi(string)+1)

    


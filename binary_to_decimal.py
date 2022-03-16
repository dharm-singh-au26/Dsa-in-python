"""
Write a program to convert Binary number (given as list) to decimal
Integer
Input: [1,0,1]
Output: 5
Explanation : -
def Convert_Binary_to_Decimal(list1)
"""
def Convert_Binary_to_Decimal(n):
    	
	num = int(n)
	dec_value = 0
	

	base = 1
	
	temp = num
	while(temp):
		last_digit = temp % 10
		temp = int(temp / 10)
		
		dec_value += last_digit * base
		base = base * 2
	return dec_value

num = "101001"
print(Convert_Binary_to_Decimal(num));




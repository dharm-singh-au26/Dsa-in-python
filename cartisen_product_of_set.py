'''
cartisen product
'''
A = [4,5,8,9]
B = [12,4,7,8]
C = [7,8,5,6]

cartisen_product = [(a,b,c) for a in A for b in B for c in C]
print(cartisen_product)
print(len(cartisen_product))
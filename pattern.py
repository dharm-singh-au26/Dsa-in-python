"""
Print the following patterns using loop :
a.
*
**
***
****
"""

line = int(input("Enter line number here :"))

for i in range (0,line+1):
    print(i*("*"))

"""
  *  
 *** 
*****
 *** 
  *  
"""
line = int(input("Enter the line number :"))
for i in range(1,line//2+2):
  print(" "*((line//2)-i+1)+"*"*(2*i-1))

  
for j in range (line//2+2,line+1):
  print(" "*(j-(line//2)-1)+"*"*(2*(line-j)+1))
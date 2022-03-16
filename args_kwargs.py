"""
args and kwargs function 

"""

def funargs (normal,*args,**kwargs):
    print(normal)
    for item in args:
        print(item)
    for key,value in kwargs.items():
        print(f"{key} is a {value}")



har = ["Ramesh","Shivam","Harish","Suresh","Ganesh"]

normal ="I am a normal argument and students are here : "

kw = { "Shivam" : "Monitor" , "Harish":"Fitness Teacher ","Suresh":"Music composer"}

funargs(normal,*har,**kw)
# funargs(*har)
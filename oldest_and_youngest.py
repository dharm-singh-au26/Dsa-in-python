"""
Take input of age of 3 people by user and determine oldest and youngest among them.
"""
age1 = int(input("Enter age1 here :"))
age2 = int(input("Enter age2 here :"))
age3 = int(input("Enter age3 here :"))

if age1 > age2 :
    if age1 > age3 :
        print(f"oldest is age1 and age is {age1}")
        if age2 > age3:
            print(f"youngest is age3 and age is {age3}")
    else:
        print(f"youngest is age2 and age is {age2}")
elif age2 > age3:
    print(f"oldest is age2 and age is {age2}")
    if age1>age3 :
        print(f"youngest is age3 and age is {age3}")
    else:
        print(f"youngest is age1 and age is {age1}")
elif age3>age1 :

    print(f"oldest is age3 and age is {age3}")
    
    if age2 > age1:
        print(f"youngest is age1 and age is {age1}")
    else:
        print(f"youngest is age2 and age is {age2}")
else:
    print("All are equal")

    
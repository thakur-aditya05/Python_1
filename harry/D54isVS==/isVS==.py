# Full path:
# is compare values and address (similar to === in js)
# == compare only values


a=4
b="4"
print(a==b) # True
print(a!=b) # False
print(a is b) # False
print(a is not b) # True




a=[1,2,43]
b=[1,2,43]
print(a==b) # True
print(a!=b) # False
print(a is b) # False
print(a is not b) # True








a=3
b=3
print(a==b) # True
print(a!=b) # False
print(a is b) # True 
print(a is not b) # False




a="aditya"
b="aditya"
print(a==b) # True
print(a!=b) # False
print(a is b) # True 
print(a is not b) # False


a=None
b=None
print(a==b) # True , a and b dono smae address ko hi point kr rahe hai koi ki non mutable hai(1,2,3,4,5,6,7,8,9,10)
print(a!=b) # False
print(a is b) # True 
print(a is not b) # False


a=(1,2,3,4,5,6,7,8,9,10)
b=(1,2,3,4,5,6,7,8,9,10)
print(a==b) # True
print(a!=b) # False
print(a is b) # True 
print(a is not b) # False













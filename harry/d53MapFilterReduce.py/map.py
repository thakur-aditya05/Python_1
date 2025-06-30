# map 
# filter
# reduce 


# map function 
def cube(x):
    return x**3

l=[1,2,3,4,5]
newL=[] # new empty list 
for item in l:
    newL.append(cube(item))
print(newL) # [1, 8, 27, 64, 125]

newl2=map(cube,l) #return map opbect
print(newl2) # <map object at 0x0000020E3F3F8C40>
for i in newl2:
    print(i) # 1 8 27 64 125
print(list(newl2)) # [1, 8, 27, 64, 125]


















































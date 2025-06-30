# key value pairs 
dist={
    "name":"aditya",
    "age":19,
    "isStudent":True,
    "height":5.9,
    
    1:"tanmay",
    2:"sachin",
    True:"rahul",
    4:"aditya"
}


# they all gives error if these keys are not present in dicrionaries

print(dist)
print(dist["name"])
print(dist["age"])
print(dist["isStudent"])
print(dist["height"])
print(dist[1])
print(dist[2])
print(dist[True])


# they all NOTE  gives error if these keys are not present in dicrionaries

print(dist)
print(dist.get("name"))
print(dist.get("age"))
print(dist.get("isStudent"))
print(dist.get("height"))
print(dist.get(1))
print(dist.get(2))
print(dist.get(True))
print(dist.get(3))

# ordered
# changeable
# indexed
# no duplicate values
# mutable
# iterable
# hashable


#now how to acccess all key  or only values 
print(dist.keys())
print(dist.values())


dist={
    "name":"aditya",
    "age":19,
    "isStudent":True,
    "height":5.9,
    
    1:"tanmay",
    2:"sachin",
    True:"rahul",
    4:"aditya"
}

for key in dist.keys():
    print(key)
    print(dist[key])

for key in dist.keys():
    print(f"the values of key {key} is {dist[key]}")
    
# 
print(dist.items())

#
for key,value in dist.items():
    print(f"the values of key {key} is {value}")
    
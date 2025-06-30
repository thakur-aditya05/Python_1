#https://docs.python.org/3/tutorial/datastructures.html

ep1={
    122:45,
    123:89,
    567:69,
    
}
ep2={
    222:67,
    566:90,
}
# dictinory items ordered 
# ep1.update(ep2)

print(ep1)

ep1.clear()
print(ep1)


ep1.pop(122)
ep1.popitem()


# del ep1 
# print(ep1)

del ep1[122] 
print(ep1)




# update 
ep1.update({"age":20})























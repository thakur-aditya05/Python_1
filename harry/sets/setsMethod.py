# ppuri mathmatics me set ek collection hoti hai jo ki unique hoti hai aur unordered hoti hai

s1={1,2,3,4}
s2={3,4,5,6}
print(s1.union(s2))
print(s1)
print(s2)

print(s1.intersection(s2)) # s2 and s1 me jo common cheeze hongi wo print hongi  unka set bn jata hai 


print(s1.difference(s2))

print(s1.symmetric_difference(s2)) #wo value jo common nahi hai 

print(s1.isdisjoint(s2)) #agar s1 and s2 me koi bhi common value nahi hai to true return karega
print(s1.issubset(s2))
print(s1.issuperset(s2))


s1={1,2,3,4}
s2={3,4,5,6}
s1.add(5) # add 7 in s1
print(s1,s2)


s1.remove(5)  # remove 5 from s1 else show error
print(s1,s2)


s1.discard(5) # remove 5 from s1 else show no error
print(s1,s2)

# pop  koi bhi random value remove kar deta hai
print(s1.pop())
print(s1,s2)

#update 
s1={1,2,3,4}
s2={3,4,5,6}
print(s1.update(s2)) # s1 me s2 ko add kar deta hai
print(s1)
print(s2)
print(s1.intersection_update(s2)) # s1 me s2 ke common cheeze add ho jati hai
print(s1)
print(s2)







# del
s1={1,2,3,4}
s2={3,4,5,6}
print(s1)
print(s2)
del s1
del s2
print(s1)
print(s2)

# clear

s1={1,2,3,4}
s2={3,4,5,6}
print(s1)
print(s2)
s1.clear()
s2.clear()
print(s1)
print(s2)


# check if the item exists in the set
info={"aditya", 19, False, 5.9, 19}
print("aditya" in info)
if "aditya" in info:
    print("print aditya singh is present in the set")
else:
    print("aditya singh is not present in the set")




























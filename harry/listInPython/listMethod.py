l=[11,45,1,23,45]
print(l)
l.append(100) # add 100 athe end of list 
l.sort(reverse=True) 
print(l)
l.reverse() #reverse the list 
print(l)
print(l.count(45)) # count the number of occurence 
print(l.index(45)) # give the 1st index of occurence 
l.insert(2,1000) #insert 1000 at 2 index
print(l)

# reference copy 
m=l
m[2]=100
print(l)
print(m)

# deep copy 
m=l.copy()
m[2]=10210
print(l)
print(m)

# extend method in list 
m=[1,2,3,4,5]
n=[100,200,300,400,500]

m.extend(n)
n.extend(m)
p=m+n

print(p)
print(m)
print(n)
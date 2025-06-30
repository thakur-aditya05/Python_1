# to manupalte tuples  change it to list and then changes and again convert it to tuples

countriesTuple=("india","usa","uk","russia","china")
print(countriesTuple)

tempList=list(countriesTuple) #typecasting tulpe to list

print(type(countriesTuple))
print(type(tempList))
tempList.append("australia")
tempList.pop(3)
tempList[2]="japan"

countriesTuple=tuple(tempList)# typecasting list to tuple

print(type(countriesTuple))
print(countriesTuple)


contriesTuples1=("pakistan","nepal","bhutan","srilanka")
print(contriesTuples1)
countriesTuple2=("india","usa","uk","russia","china")
print(countriesTuple2)
countriesTuple3=contriesTuples1+countriesTuple2
print(countriesTuple3)


# 
tuples1=(1,2,3,4,5)
res=tuples1.count(1) # give thhe count of 1 in tuples 
print('count of 3 in tuples1 is:',res) 

res=tuples1.index(3) # gives the index of 3 in tuples 
print('index of 3 in tuples1 is:',res)

res=tuples1.index(3,4,8) # gives the index of 3 in tuples
print('index of 3 in tuples1 is:',res)

res=len(tuples1) # gives the length of tupeles 
print('length of tuples1 is:',res)



# convert the tuples into the list and then change or aply the list method the list and then again convert it into tuples












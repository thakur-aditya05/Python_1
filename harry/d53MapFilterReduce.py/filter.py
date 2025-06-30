# filter 

# list kko filter kiya jayega ek condition se 


def filterFuncion(a):
    return a>2
newList=list(filter(filterFuncion,[1,2,3,4,5,6,7,8,9,10]))
print(newList) # [3, 4, 5, 6, 7, 8, 9, 10]
newList2=filter(lambda a:a>2,[1,2,3,4,5,6,7,8,9,10])
print(list(newList2)) # [3, 4, 5, 6, 7, 8, 9, 10]
# filter function will return the filter object
#according to the argument passed in the filter function  



















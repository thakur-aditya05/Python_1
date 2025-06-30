# tuples are ordered collection of data items
# they are immutable    
# list and tuples are same but tuples are immutable

tuples=(1,2,3,4,5)
tuples[0]=100 # tuples are immutables in nature 
print(type(tuples))
print(tuples)
print(tuples[0])
print(tuples[1])
print(tuples[2])


tuples2=("red","green","blue","yellow","cyan","magenta","black","white")
print(type(tuples2))
print(tuples2)
print(tuples[-1]) #  len(tuples)-1
print(tuples[-2]) #  len(tuples)-2

if "red" in tuples2:
    print("yes 342 is present in this tuples ")
else:
    print("not preent ")
    

# slicing ke baad ek naya tuples milta hai and original tuples change nahi hota
# after every method on tuple  a new tuple is formed


tupDu=tuples2[2:5]
print(tupDu)



tuples=(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)
print(tuples)
print(tuples[:])      # tuples[0:len(tuples)]                 # all the element of tuples
print(tuples[3:])
print(tuples[:3])
print(tuples[2:-2])
print(tuples[2:8:2]) 

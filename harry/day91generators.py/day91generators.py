# generatrs are different from list 
# directly ye cheezy execute nahi krta hai on the fly(mauke pe kaam krta hai ) ye cezon ko execute krta hai 

def my_generators():
    for i in range(5000):
        yield i

gen =my_generators()
print(next(gen))
print(next(gen))
print(next(gen))





# ways 2 to use 
def my_generators():
    for i in range(5000):
        yield i
gen =my_generators()
for j in gen:
    print(j)

# list vs generators 
# generators are lazy wo kaam ko talte rahte hai wo jitna kaam abhi ka hota hai wo abhi kr dete hai baki ka kaam baad ke liye chhor dete hai 
# generatos are may be complex inn nature 









# new to walrus operature
a=True 
# print(a=False) # not possible
print(a:=False) # kisi expression ke under jake kisi variable ki value change kr rahe hai 


l=[1,2,3,4,5]
while(n:=len(l))>0:
    print(l.pop())





# ye thi aam jindagi cheezo ko krne ki 

foods=list()
while True:
    food=input("what food do you like?: ")
    if food=="quit":
        break
    foods.append(food)








# simply we can say key bade expression ki value ko calculate kr ke ek variable ko assign karata hai 
# ye thi mentos jindagi cheezo ko krne  ki 

foods=list()
while (food:=input("what food do you like?: ")) !="quit":
    foods.append(food)










data = input("Enter something: ")
if len(data) > 5:
    print("Long input")


if (data := input("Enter something: ")).strip():
    print(f"You entered: {data}")


#shutil.rmtree(path) # pura folfder ya file  delete kr dega 
shutil.rmtree("mytuturial")

if (data := input("Enter something: ")).strip():
    print(f"You entered: {data}")










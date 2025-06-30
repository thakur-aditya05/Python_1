# linter 
# normal way for doiing the same 
# just it will give u a index number for iteration
marks =[12,114,55,4,77,8,1,5,2]
index=0
for mark in marks:
    print(mark)
    if index==3 :
        print("harry, awesome!")
    index +=1




marks =[8,1,5,2]

for index,mark in enumerate(marks):
    print(mark)
    if index==3 :
        print("harry 2, awesome!")
        


# 
marks =[8,1,5,2,1,2,3,4,5]

for v in enumerate(marks):
    print(v)
    if index==3 :
        print("harry 3, awesome!")




# 
marks =[8,1,5,2,1,2,3,4,5]

for v in enumerate(marks,start=1):
    print(v)
    if index==3 :
        print("harry 4, awesome!")
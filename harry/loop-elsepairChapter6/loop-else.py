# The else in a loop is executed only if the loop completes its full iteration without encountering a break.
# If the loop is exited early (via break), the else block will not be executed.

for i in range(5):
    print(i)
else:
    print("i succesfully completed all iterartion ")
    
for i in range(6):
    print(i)
    if i==4:
        break
else:
    print("loop is breaked at a ppoint ")
    

i=0
while i<7:
    print(i)
    i=i+1
    if i==4:
        break
else:
    print("again loop is breaed at a time ")
    

    

i=0
while i<7:
    print(i)
    i=i+1

else:
    print("sorry it will not work")


for x in range(5):
    print("iterartion no {} in for loop".format(x+1))
else:
    print("else block in loop ")
print("out of loop")
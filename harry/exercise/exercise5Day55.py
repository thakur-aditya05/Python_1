# snake water Gun game

# hint 
#             s w g
# computer=   0 1 2
# palayer=s 0 D W l
#         w 1 l D W
#         g 2 W l D

import random 
def check(comp,user):
    if comp==user:
        return 0
    if(comp==0 and user==1):
        return -1
    if(comp==1 and user==2):
        return -1
    if(comp==2 and user==0):
        return -1
    return 1

comp=random.randint(0,2) # will generate random integer 
user=int(input("0 for snake, 1 for water and 2 for gun")) # user's input

score=check(comp,user)
print("you : ",user)
print("computer :",comp)

if(score==0):
    print("its s draw")
elif(score==-1):
    print("you loose")
else:
    print("you won")





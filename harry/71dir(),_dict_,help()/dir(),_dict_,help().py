# anjaan class
x=[1,2,3,4]
print(dir(x)) # puri details deta hai i kon kon si methhod hai 
# it also return dundar method 

x=(1,2,3,4)
print(dir(x)) # puri details deta hai i kon kon si methhod hai 

# now what is __dict__
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        self.verson=1

p=Person("john",30)
print(p.__dict__) # saari cheeze jo ki self ke distnary ke form me conver t ho jate hai 


# now ab baari aaati hai help()
print(help(Person)) # give every thing about class about histroy physics and geography  






























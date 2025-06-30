# @ static method decorators ----> baar baar hrr instance ke liye chnage nahi hota kyo ki wo hrr instance ke liye form nahi hota hai eo ek baar bnta hai and will be used by alll the object 
# but but they cant access and modifyy class states& general use for utitlity 
class Person:
    name="anonymous"
    def changeName(self,name):
        self.name=name 

p1=Person()
p1.changeName("aditya singh") # i m trting to change name of class atrribut but will leads to create name of instance and will not change "'name="anonymous"'"
print(p1.name)

# inderect way to chnage class atrribute is 
class Person:
    name="anonymous"
    def changeName(self,name):
        Person.name=name 

p1=Person()
p1.changeName("aditya singh") # i m trting to change name of class atrribut but will leads to create name of instance and will not change "'name="anonymous"'"
print(p1.name)





# 2nd inderect way to chnage class atrribute is 
class Person:
    name="anonymous"
    def changeName(self,name):
        self.__class__.name=name

p1=Person()
p1.changeName("aditya singh") # i m trting to change name of class atrribut but will leads to create name of instance and will not change "'name="anonymous"'"
print(p1.name)




# originally class attribute ko chnage krme ke liye class method ko use krte hai 
class Person:
    name="anonymous"
    
    # class method are used to change the class attribute directly 
    def changeName(cls,name):
        cls.name=name

p1=Person()
p1.changeName("aditya singh") # i m trting to change name of class atrribut but will leads to create name of instance and will not change "'name="anonymous"'"
print(p1.name)



# @staticmethod  (ye kuch bhi change nahi krte hai 
# @classmethod(class  as the 1st argument aaraha hai to change the class method or to from class attribute  )
# insatance method (self as the 1st argument aaraha hai to make object instance method      )


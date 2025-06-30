# Constructor in Python
# Constructor is a special type of method (function) which is used to initialize the instance members of the class from outside for perticular object 
# it alwats return none 

#parameterized constructor and non parameterized( Deafult ) constructor
class Person:
    def __init__(self): #constructor deafult constructor non  parameterized constructor
        print("hey i m person's constructor")
        
    def info(self):
        print("f{self.name} is a {self.occupation}")


a=Person() #person jo ki class hai wo automatically pass ho jayegi as  a 1st argument named as self




class Person:
    def __init__(self,name,occ): #constructor deafult constructor non  parameterized constructor
        print("hey i m person's constructor")
        self.name=name
        self.occupation=occ
        
    def info(self):
        print("f{self.name} is a {self.occupation}")


a=Person("aditya","student") #person jo ki class hai wo automatically pass ho jayegi as  a 1st argument named as self and name as aditya and occ as student
a.info() # aditya is a student
b=Person("nikita","doctor") #person jo ki class hai wo automatically pass ho jayegi as  a 1st argument named as self and name as nikita and occ as doctor
b.info() # nikita is a doctor




class Math:
    def __init__(self, num):
        self.num=num
    def addToNum(self,n):   # this is class method i.e associated with class 
        self.num=self.num+n

a=Math(5)
print(a.num)
a.addToNum(6)
print(a.num)


# just i want to create a utility("utility" generally refers to reusable helper functions, modules, or scripts that perform common tasks. These utility functions help in code reusability, modularity, and efficiency.) 
class Math:
    def __init__(self, num):
        self.num=num
    def addToNum(self,n):   # this is class method i.e associated with class 
        self.num=self.num+n
        
    # there is no need to pass self in this method 
    # this method can be used to get call from or name of class method 
    # ye class ke variable ko to use kr raha hai but self directly pass nahi ho raha hai 
    # a and b ko use kr raha hai but ye class ka part hai  
    @staticmethod
    def add(a,b):
        return a+b

a=Math(5)
print(a.num)
a.addToNum(6)
print(a.num)

print(Math.add(7,2)) 
print(a.add(7,2))






























# private like attribute and 

class Account:
    def __init__(self,acc_no,acc_pass):
        self.acc_no=acc_no
        
    # undercsore lagana hota hai to make private 
        self.__acc_pass=acc_pass  # __acc_pass become private and like wise non accessale from outside of the class
    def reset_pass(self):
        print(self.__acc_pass) # yes ke under to accessable hai but bahar nahi hai 

acc1=Account("12456","abcde")
print(acc1.acc_no)
print(acc1.acc_pass) #  non accesable from outside of thr class 
print(acc1.reset_pass()) 





class Person:
    __name="anonymous"
    def __hello():
        print("hello person")
    
    def welcome(self):
        self.__hello()  #priivate tye ko access krna possible from the class

p1=Person()



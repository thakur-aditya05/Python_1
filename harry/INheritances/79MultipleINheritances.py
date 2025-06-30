class Employee:
    def __init__(self,name):
        self.name=name
    
class Dancer:
    def __init__(self,dance):
        self.dance=dance

class DancerEmployee(Employee,Dancer):
    def __init__(self,dance,name):
        self.dance=dance
        self.name=name

o=DancerEmployee("kathak","shivani")
print(o.name)
print(o.dance)
        






class Employee:
    def __init__(self,name):
        self.name=name
    def show(self):
        print(f"the name is {self.name}")
        
class Dancer:
    def __init__(self,dance):
        self.dance=dance
    def show(self):
        print(f"the dance is {self.dance}")

class DancerEmployee(Employee,Dancer):
    def __init__(self,dance,name):
        self.dance=dance
        self.name=name

o=DancerEmployee("kathak","shivani")
print(o.name)
print(o.dance)
o.show()        














class Employee:
    def __init__(self,name):
        self.name=name
    def show(self):
        print(f"the name is {self.name}")
        
class Dancer:
    def __init__(self,dance):
        self.dance=dance
    def show(self):
        print(f"the dance is {self.dance}")

class DancerEmployee(Dancer,Employee):
    def __init__(self,dance,name):
        self.dance=dance
        self.name=name

o=DancerEmployee("kathak","shivani")
print(o.name)
print(o.dance)
o.show()        












# -----------------------------

class Employee:
    def __init__(self,name):
        self.name=name
    def show(self):
        print(f"the name is {self.name}")
        
class Dancer:
    def __init__(self,dance):
        self.dance=dance
    def show(self):
        print(f"the dance is {self.dance}")

class DancerEmployee(Employee,Dancer):
    def __init__(self,dance,name):
        self.dance=dance
        self.name=name

o=DancerEmployee("kathak","shivani")
print(o.name)
print(o.dance)
o.show() 
print(DancerEmployee.mro()) # priority of finding in class 
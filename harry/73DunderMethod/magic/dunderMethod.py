# magic and dunder method 
class Employee:
    name="harry"
    def __len__(self):
        i=0
        for c in self.name:
            i=i+1
        return i
e=Employee()
print(e.name)
print(len(e))





#  
class Employee:
    name="harry"
    def __len__(self): #3 iss function ko call krte samaye keval "len keyword use krna padega "
        i=0
        for c in self.name:
            i=i+1
        return i
    
    def __str__(self):
        return f"the name of the employee is {self.name} str"
    def __repr__(self):
        return f"Employee('{self.name}')"
    def __call__(self):
        print("hey I am good")

e=Employee()
print(e.name)
print(len(e))
print(str(e))
print(repr(e))
e()



































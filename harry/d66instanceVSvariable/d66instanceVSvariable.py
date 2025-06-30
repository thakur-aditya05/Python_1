class Employee:
    def __init__(self,name):
        self.name=name
        
    def showDetails(self):  # we are sending one argument 
        print(f"the name of the Employee is {self.name}")

    def showGreet():  # we are  not sending any argument 
        print(f"the name of the employee is ")

emp1=Employee("harry")
Employee.showDetails(emp1) # this is written as 
emp1.showDetails()  # ---> converted to "Employee.showDetails(emp1)" yani ek argument pass on ho raha hai 


emp1.showGreet()
Employee.showGreet(emp1) # this was  




# noow deffrance b/w is instance and class 

# instance variable hai 
class Employee:
    def __init__(self,name):
        self.name=name
        self.raise_amount=0.02 # instance variable yani hrr object ke saath asscoiated hoti hai 
    def showDetails(self):  # we are sending one argument 
        print(f"the name of the Employee is {self.name} and his raise is {self.raise_amount}")

emp1=Employee("harry")
emp1.raise_amount=0.3 # we are changing araise amount for employess 1 yani of harry and will nort effect others raise amount 
emp1.showDetails() 
emp2=Employee("rohan")
emp2.showDetails()



# class variable 
class Employee:
    company_name="apple america " # ye class varible hai  
    def __init__(self,name):
        self.name=name
        self.raise_amount=0.02 # instance variable yani hrr object ke saath asscoiated hoti hai 
    def showDetails(self):  # we are sending one argument 
        print(f"the name of the Employee is {self.name} and his raise is {self.raise_amount} working in {self.company_name}")

emp1=Employee("harry")
emp1.raise_amount=0.3 # we are changing araise amount for employess 1 yani of harry and will nort effect others raise amount 
emp1.company_name="apple india" # idhar se ye defined kr diya ki company name for harry appale india ho jaye 
emp1.showDetails() 

print(Employee.company_name)
Employee.company_name="google" 
print(Employee.company_name)

emp2=Employee("rohan")
emp2.showDetails() # hamne koi company name nahi banya hai rohan ke liye yani class varible smne aayega i.e apple america 






# just example
class Employee:
    company_name="apple america " # ye class varible hai i.e if company name is not given for particular object then this class varable will be prented  
    noOfEmployees=0
    def __init__(self,name):
        self.name=name
        self.raise_amount=0.02 # instance variable yani hrr object ke saath asscoiated hoti hai 
        Employee.noOfEmployees += 1    # class varible ki value ko acess kr ke +1 kr dena initial value ke respect me 
    def showDetails(self):  # we are sending one argument 
        print(f"the name of the Employee is {self.name} and his raise is {self.raise_amount} working in {self.company_name} having number of {self.noOfEmployees}")

emp1=Employee("harry")
emp1.raise_amount=0.3 # we are changing araise amount for employess 1 yani of harry and will nort effect others raise amount 
emp1.company_name="apple india" # idhar se ye defined kr diya ki company name for harry appale india ho jaye 
emp1.showDetails() 

print(Employee.company_name)
Employee.company_name="google" 
print(Employee.company_name)

emp2=Employee("rohan")
emp2.showDetails() # hamne koi company name nahi banya hai rohan ke liye yani class varible smne aayega i.e apple america 










































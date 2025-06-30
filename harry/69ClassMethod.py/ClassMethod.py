# class are used to create custom data type 
class Employee:
    company="apple" # class variable hai yani jis object ke liye company varible user sended nahi hoga tb tb yahi wala use kiya jayega 
    def show(self):
        print(f"the name is {self.name} and company is {self.company}")
    # lets create the function which helps in  changeing the  objcet's company  
    def changeCompany(cls, newCompany):
        cls.company=newCompany

e1=Employee() # ek varible bana company ke naam ka 
e1.name="harry" 
e1.show()
e1.changeCompany("tesla") # isse class varible nah change hota hoga bs e1 employi ke liye bs company name change ho jayega 
e1.show()
print(Employee.company)# class varible chnage nahi hua hai line e1.changeCompany("tesla")  ke karan bs object ke liye instance me convert ho gaya hai 


# to kaise chnage kare class varible ko taki wo class varibla sbke liey change ho jaye 
# by using @classmethod




# class are used to create custom data type 
class Employee:
    company="apple" # class variable hai yani jis object ke liye company varible user sended nahi hoga tb tb yahi wala use kiya jayega 
    def show(self):
        print(f"the name is {self.name} and company is {self.company}")
    # now lets change class variblle name finnaly for all  object 
    
    @classmethod
    #abi issko 1st argument as the class milega (yaha pe Employee jo ek class hai)
    # without @classmethod by default argumrn object instance mil raha tha 
    # cls-> class as the argument ja raha hai 
    # ye tabhi use krna hai jb class ki cheeze change krna chahte ho aap 
    def changeCompany(cls, newCompany):
        cls.company=newCompany

e1=Employee() # ek varible bana company ke naam ka 
e1.name="harpreet" 
e1.show()
e1.changeCompany("tata") # isse class varible nah change hota hoga bs e1 employi ke liye bs company name change ho jayega 
e1.show()
print(Employee.company)# class varible chnage ho  hua hai line e1.changeCompany("tesla")  ke karan bs object ke liye instance me convert ho gaya hai 








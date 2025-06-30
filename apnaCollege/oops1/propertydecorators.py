# prperty method
class Student:
    def __init__(self,phy,chem,math):
        self.phy=phy
        self.chem=chem
        self.percentage=str((self.phy+self.chem+self.math)/3)+"%"

stu1=Student(98,97,100) 
print(stu1.percentage) # teen subject ke marks diye 

stu1.phy=97 # i cangeed the physics marks to 97 will my percentage will change or not 
print(stu1.phy) # number got change 
print(stu1.percentage)# percentage still not got change 


# to issko dynamic banane ke liye 
# ye kaam karega  always 
# prperty method
class Student:
    def __init__(self,phy,chem,math):
        self.phy=phy
        self.chem=chem
        self.percentage=str((self.phy+self.chem+self.math)/3)+"%"
    def calPercentage(self):
        self.percentage=str((self.phy+self.chem+self.math)/3)+"%" 
stu1=Student(98,97,100) 
print(stu1.percentage) # teen subject ke marks diye 

stu1.phy=86
print(stu1.phy)
print(stu1.calPercentage())






# but originally ye krna hota hai hamesh hameshha ke liye 
class Student:
    def __init__(self,phy,chem,math):
        self.phy=phy
        self.chem=chem
    
    @property # iske kara  ye dynamic bn jayega yani thodda sa bhi chnage pure me refeclt kr dega 
    def percentage(self):
        return str((self.phy+self.chem+self.math)/3)+"%"
    
stu1=Student(98,97,100) 
print(stu1.percentage) # teen subject ke marks diye 

stu1.phy=86
print(stu1.percentage())








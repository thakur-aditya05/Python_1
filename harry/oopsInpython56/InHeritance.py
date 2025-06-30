class Employee:
    def __init__(self,name,id):
        self.name=name
        self.id=id
    def showDetails(self):
        print(f"the name of employes: {self.id} is {self.name}")

e1=Employee("aditya",1)
e1.showDetails()
e2=Employee("nikita",2)
e2.showDetails()


# ---------------------------------------------------------------------------------------------------------------
# if i want to change the programer as a name of class without effecting else thing 

class Programer(Employee):
    def showLanguage(self):
        print("the deafult language is python")

e3=Programer("aman",4000)
e3.showDetails()
e3.showLanguage()

# inheritance are of 5 types 
# single 






































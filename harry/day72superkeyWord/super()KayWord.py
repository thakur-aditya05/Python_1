class Employee:
    def __init__(self,name,id):
        self.name=name
        self.id=id

class Programer:
    def __init__(self,name,id,lang):
        self.name=name
        self.id=id
        self.lang=lang

Rohan=Employee("Rohan das","420")
Harry=Programer("Harry","2345","python")
print(Harry.name)
print(Rohan.name)


# while ussing super key word as constructor 
class Employee:
    def __init__(self,name,id):
        self.name=name
        self.id=id

class Programer(Employee):
    def __init__(self,name,id,lang):
        super().__init__(name,id)
        self.lang=lang

# 

Rohan=Employee("Rohan das","420")
Harry=Programer("Harry","2345","python")
print(Harry.name)
print(Rohan.name)
print(Rohan.id)
print(Rohan.lang)
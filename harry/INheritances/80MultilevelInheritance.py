# a--->b--->c(pota)
class Animal:
    def __init__(self,name,species):
        self.name=name
        self.species=species
    def show_details(self):
        print(f"Name :{self.name}")
        print(f"Species : {self.species}")

class Dog(Animal):
    def __init__(self,name,breed):
        Animal.__init__(self,name,species="dog")
        self.breed=breed
    def show_details(self):
        Animal.show_details(self)
        print(f"Breed: {self.bread}")

class GoldenRetriver(Dog):
    def __init__(self,name,color):
        Dog.__init__(self,name,breed="Golden Retriver")
        self.color=color
    def show_details(self):
        Dog.show_details(self)
        print(f"color: {self.color}")

o=GoldenRetriver("tommy","Black")
o.show_details()  
print(GoldenRetriver.mro())

# print(f"Name :{self.name}")
# print(f"Species : {self.species}")
# print(f"Breed: {self.bread}")
# print(f"color: {self.color}")




o=Dog("tommy","Black")
o.show_details()  
# print(f"Name :{self.name}")
# print(f"Species : {self.species}")
# print(f"Breed: {self.bread}")
















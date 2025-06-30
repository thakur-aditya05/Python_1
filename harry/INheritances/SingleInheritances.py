class Animal:
    def __init__(self,name,species):
        self.name=name
        self.species=species
    def make_sound(self):
        print("sound made by the animals")

class Dog(Animal):
    def __init__(self,name,bread):
        Animal.__init__(self,name,species="Dog")
        self.breed=bread
    def make_sound(self):
        print("Barks")


d=Dog("Dog","Dogger")
d.make_sound()


a=Animal("Dog","Dog")
a.make_sound() 




# quick quiz make the cat class and implement inharitances 






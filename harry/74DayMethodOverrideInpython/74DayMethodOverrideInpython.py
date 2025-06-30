# parent class ke method ko child class ke basis pe redifined krna padta 

class Shape: 
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def area(self):
        return self.x*self.y

rec=Shape(3,5)
print(rec.area())

# -----------------------------------

class Shape: 
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def area(self):
        return self.x*self.y
class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
        super().__init__(radius,radius)
        
    def area(self):
        return 3.14*super().area() # super ka matlab ek level upper jaao and area lekr aao 

circle=Circle(3)
print(circle.area())






















# The questions are:

# Define a Circle class to create a circle with radius r using the constructor.
# Define an Area() method to calculate the area of the circle.
# Define a Perimeter() method to calculate the perimeter of the circle.

# Define an Employee class with attributes role, department, and salary.
# This class should have a showDetails() method.
# Create an Engineer class that inherits properties from Employee and has additional attributes: name & age.






class Circle:
    def __init__(self,radius):
        self.radius=radius
    
    def area(self):
        return (22/7)*self.radius**2
    
    def perimeter(self):
        return 2*(22/7)*self.radius

c1=Circle(21)





# The question is:
# Create a class called Order which stores an item and its price.
# Use the Dunder function __gt__() to define the comparison:
# order1 > order2 if price of order1 is greater than price of order2.
class Order:
    def __init__(self,item,price):
        self.item=item
        self.price=price
    def __gt__(self,odr2): # similarly 
        return self.price>odr2.price

odr1=Order("chips",20)
odr2=Order("tea",10)
print(odr1>odr2)#true 













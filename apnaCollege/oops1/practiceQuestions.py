# Create a class named Student
# Use a constructor (__init__ method) that takes four arguments:
# name (student's name)
# Marks of three subjects
# Create a method inside the class that calculates and prints the average of the three subject marks.

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    
    # this is not possible 
    def hello():
        print("hello")
    
    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("hi", self.name, "your avg score is:", sum / 3)

s1 = Student("tony stark", [99, 98, 97])
s1.get_avg()

s1.name = "ironman"
s1.get_avg()













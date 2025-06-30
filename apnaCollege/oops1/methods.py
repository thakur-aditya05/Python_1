# class ke under do cheeze htoi hai 
# varibale  (class and object )
# method 

class Student:
    college_name="abc coleege"
    
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    
    def welcome(self):# self arumnet is most important 
        print("welcome")
        
    def get_marks(self):
        return self.marks
    
s1=Student("aditya",97)
s1.welcome()
print(s1.get_marks())
# del keyword
del s1.className

class Student:
    COLLEGE_NAME="MANIT" # ye class atrribute hai yani 10000 object creation ke baad bhi keval ek class attribute create hoga  hi create hoga 
    name="anonymuoys" #class atribute 
    def __init__(self,name,marks):
        self.name=name # s1.name s2.name s3.name s4.name s5.name (object ke under jo naya name name ka varible create hua hai uski value)
        self.mark=marks # ye cb 1000object create hone ke baad 1000 baar create honge 
        print("adding new student in database....")
s1=Student("aditya",97)
print(s1.name,s1.marks)
print(Student.COLLEGE_NAME) #class atribute 
del s1.name # to delete object of of the particular class 
s1=Student("aditya",97)

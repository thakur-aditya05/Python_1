class Student:
    name="karan"
    def __init__(self):
        print("adding new student in database....")
        print(self) # kuch orr nahi s1 ko hi point out kr raha hai (self==s1)
s1=Student()
print(s1)



class Student:
    name="karan"
    def __init__(self,name,marks):
        print("adding new student in database....")
        print(self)  
        self.name=name # s1.name s2.name s3.name s4.name s5.name (object ke under jo naya name name ka varible create hua hai uski value)
        self.mark=marks
s1=Student("aditya",97)
print(s1.name,s1.marks)




class Student:
    # deafult constructor
    def __init__(self):
        pass
    
    # parametric constructor
    # jo object creartion krte samaye hamre constructor ke saath match kareag wahi constructor chalega   
    def __init__(self,name,marks):
        self.name=name # s1.name s2.name s3.name s4.name s5.name (object ke under jo naya name name ka varible create hua hai uski value)
        self.mark=marks
        print("adding new student in database....")
s1=Student("aditya",97)
print(s1.name,s1.marks)
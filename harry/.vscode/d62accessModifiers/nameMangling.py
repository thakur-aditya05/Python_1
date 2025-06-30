class Student:
    def __init__(self,age,name):
        self.__age=age # private variable indicator
    def __funName(self): # indication of private function
        self.y=34
        print(self.y)

class Subject(Student):
    pass

obj=Student(21,"harry")
obj1=Subject()
print(dir(obj))


#calling by object of class student 
print(obj.__age)
print(obj.__funName())
#calling by object of class student 
print(obj1.__age)
print(obj1.__funName())


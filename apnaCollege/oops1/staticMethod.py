# StaticMethod 
# self reperent krta hai to the class 
# class level pe jo method use hote hai usnko bolte hai static method 
# with help of decoraters  function we convert this function to a static method 
# 
# static method 
# these ar the function who take function as the inpt and reeturn as well input 
# static decoraters convert self based method into classs method 
# self always represent object formed 

class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    @staticmethod
    def hello():
        print("hello")
    
    def get_avg(self):
        pass

s1=Student("tony strks",[99,98,97])
s1.get_avg()
    
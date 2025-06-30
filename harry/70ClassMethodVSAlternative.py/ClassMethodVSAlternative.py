# classmethod ko as the  alternativ constructor 

class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
e=Employee("harry",1200)
print(e.name)
print(e.salary)


# ab naya trika ki if information is like aise di hui hai to "string1= harry-1200"
string="aditya-3000"
e2=Employee(string.split("-")[0],string.split("-")[1]) #string.split("-") will return list of words with saparated by , on the basis of "-"
print(e2.name)
print(e2.salary)
# but ye kind of non readable hai bade format level pr to issko 
# to isske liye 


class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    
    
    @classmethod
    # ek particular format ka data parse kr rahha hu 
    # yani aane wala hrr class format data jo string format ka hoga uske liye ye parsing ka kaam krta hau 
    def fromStr(cls,string):
        return cls(string.split("-")[0],string.split("-")[1])
string="aditya-3000"
e=Employee(string)
print(e.name)
print(e.salary)





# one more example
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
    @classmethod
    def from_string(cls,string): # cls variable Employee ko pointout kr raha hai 
        name,age=string.split(",")
        return cls(name,int(age)) # this is written is like Employee(name,int(age) to aage smjha ja skta hai yani iss line ke baad duabara  def __init__(self,name,age): line chaleg8i 

person=Person.from_string("John Doe,30")
print(person.name,person.age)


# "12"+6 ==.wrong
# "12"+"6"==wrong 

























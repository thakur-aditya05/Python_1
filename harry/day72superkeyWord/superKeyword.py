class ParentClass:
    def parent_method(self):
        print("this is parent method")

class ChildClass(ParentClass):
    def child_method(self):
        print("this is the child method")
        super().parent_method()

child_object = ChildClass()
child_object.child_method()
    
# super ka matlab bs ek kadam upper jao and parent class me jao orr waha pe jake iss naam ke method ko call kr do 
class ParentClass:
    def parent_method(self):
        print("this is parent method")
        
class ChildClass(ParentClass):
    def parent_method(self):
        print("harry")
        super().parent_method()
    def child_method(self):
        print("this is the child method")
        super().parent_method()

child_object = ChildClass()
child_object.child_method()
child_object.parent_method()






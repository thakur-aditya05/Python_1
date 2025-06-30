# getter and setter are used to get and set the value of the attributes of the class.
# for any particular object of the class.
class MyClass:
    def __init__(self,value):
        self._value=value
        
    def show(self):
        print(f"value is {self._value}")
        
    @property
    def ten_value(self):
        return self._value*10

obj=MyClass(10)
print(obj.ten_value) # 100
obj.show() # value is 10









# lets try to change the value of the attribute of the class
obj.ten_value=67 # AttributeError: can't set attribute
obj.show() # value is 10
# we can not change the value of the attribute of the class directly



# ---------------------------------------------------------------------------------------------------------------
# hello this is the getter and setter
class MyClass:
    def __init__(self,value):
        self._value=value
        
    def show(self):
        print(f"value is {self._value}")
    
    
    # this function is used to get the value of the attribute of the class
    @property # this is the getter
    def ten_value(self):
        return self._value*10
    # this function is used to set the value of the attribute of the class
    @ten_value.setter # this is the setter
    def ten_value(self,new_value):
        self._value=new_value/10

obj=MyClass(10)
obj.ten_value=67
print(obj.ten_value) # 100
obj.show() # value is 10



















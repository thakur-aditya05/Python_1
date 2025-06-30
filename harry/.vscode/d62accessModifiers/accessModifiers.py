class employee:
    pass
a=employee()
a.emp1=5 # ye acessable hai bahar se bhi 

#public 
class employee:
    def __init__(self):
        self.name="harry"

a=employee()
print(a.name) #accessable




# private 
class employee:
    def __init__(self):
        self.__name="harry"   # __ week internal indicator which says cant be acess from outside of 

a=employee()
print(a.__name) #not accessable 
print(a._employee__name) # accessable indirectbale yani week internal indicator can be accessable 
print(a.__dir__()) # list of runnable method 

# name mangling 
print(a._employee__name) # to access private  protected 

# keval double underScore ke satth name manglink kar rahe hai 







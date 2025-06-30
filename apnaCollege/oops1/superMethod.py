class Car:
    def __init__(self,type):
        self.type=type
    @staticmethod
    def start():
        print("car started")
    @staticmethod
    def stop():
        print("car stopped..")

class ToyotaCar(Car):
    def __init__(self,name,type):
        self.name=name
        # we want to use "type" variable  of car class 
        # yani mujhe  kisi halat me Car class ka constructor yaha pe call krna padega taki "type" attribute use kr sake  
        




car1=ToyotaCar("fortuner","electric")
print(car1.start())


# super is meaans caaling parent class function 
class Car:
    def __init__(self,type):
        self.type=type
    @staticmethod
    def start():
        print("car started")
    @staticmethod
    def stop():
        print("car stopped..")

class ToyotaCar(Car):
    def __init__(self,name,type):
        super().__init__(type)
        self.name=name
        super().start() # calling parent class function 

car1=ToyotaCar("fortuner","electric")
print(car1.start())

















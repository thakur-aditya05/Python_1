# parent--->child
# single iheritance and inheritance 
class Car:
    color="white"
    @staticmethod
    def start():
        print("car started")
    @staticmethod
    def stop():
        print("car stopped..")

class ToyotaCar(Car):
    def __init__(self,name):
        self.name=name

car1=ToyotaCar("fortuner")
car2=ToyotaCar("prius")
print(car1.start())







class Car:
    color="white"
    @staticmethod
    def start():
        print("car started")
    @staticmethod
    def stop():
        print("car stopped..")

class ToyotaCar(Car):
    def __init__(self,brand):
        self.name=brand

class Fortuner(ToyotaCar):
    def __init__(self,type):
        self.type=type






car1=Fortuner("fortuner")
car2=ToyotaCar("prius")
print(car1.start())
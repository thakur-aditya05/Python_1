class Myclass:
    class_variable=0
    
    def __init__(self):
        Myclass.class_variable+=1
    def print_class_variable(self):
        print(Myclass.class_variable)

obj1=Myclass()
obj2=Myclass()

obj1.print_class_variable() #output 2
obj2.print_class_variable() #output 2

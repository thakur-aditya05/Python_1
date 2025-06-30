# @getter 
# @setter 
# are rest of the two best method decoretors 



# impliciting numbers 
print(1+2) # add
print(type(3))
print("apna"+"college") #concatinat
print(type("apna"))
print([1,2,2,3]+[1,2,2,3]) # merge
print(type([1,2,2,3]))


class Complex:
    def __init__(self,real,img):
        self.real=real
        self.img=img
    def showNumber(self):
        print(self.real,"i+",self.img,"j")
    def add(self,num2):
        newReal=self.real+num2.real
        newImg=self.img+num2.img
        return Complex(newReal+newImg)

num1=Complex(1,3)
num1.showNumber()

num2=Complex(2,5)
num2.showNumber()

# num3=num1+num2 # give error to our ans 
num3=num1.add(num2)
num3.showNumber()






















class Complex:
    def __init__(self,real,img):
        self.real=real
        self.img=img
    def showNumber(self):
        print(self.real,"i+",self.img,"j")
    def __add__(self,num2):
        newReal=self.real+num2.real
        newImg=self.img+num2.img
        return Complex(newReal,newImg)

    def __sub__(self,num2):
        newReal=self.real-num2.real
        newImg=self.img-num2.img
        return Complex(newReal,newImg)


num1=Complex(1,3)
num1.showNumber()

num2=Complex(2,5)
num2.showNumber()

numAdd=num1+num2 
numSub=num1-num2 
numAdd.showNumber()
numSub.showNumber()

class Vectors:
    def __init__(self,i,j,k):
        self.i=i
        self.j=j
        self.k=k
    def __str__(self):
        return f"{self.i}i+{self.j}j+{self.k}k"

v=Vectors(3,4,5)
print(v) 





# ab krte hai overloaddig 
class Vectors:
    def __init__(self,i,j,k):
        self.i=i
        self.j=j
        self.k=k
    def __str__(self):
        return f"{self.i}i+{self.j}j+{self.k}k"

    def __add__(self,x):
        return f"{self.i+x.i}i+{self.j+x.j}j+{self.k+x.k}k"

v1=Vectors(3,4,5)
print(v1) 
v2=Vectors(4,5,6)
print(v2) 
print(v1+v2)
print(type(v1+v2))




 
class Vectors:
    def __init__(self,i,j,k):
        self.i=i
        self.j=j
        self.k=k
    def __str__(self):
        return f"{self.i}i+{self.j}j+{self.k}k"

    def __add__(self,x):
        return Vectors(self.i+x.i,self.j+x.j,self.k+x.k)

v1=Vectors(3,4,5)
print(v1) 
v2=Vectors(4,5,6)
print(v2) 
print(v1+v2)
print(type(v1+v2))

# docs.python.org/3/reference/datamodel.html


# 
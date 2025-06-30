# lambda function is a small,
# anonymous function (jiske aap ko naam na pata hai jaise ki koii insaan mukhota pahen le ) in Python that is defined using the lambda keyword.
# It can have any number of arguments but only one expression.

def double(x):
    return x*2

double = lambda x: x*2
print(double(5)) # 10

cube=lambda x:x**3
print(cube(5)) # 125


avg=lambda x,y:(x+y)/2
print(avg(5,10))# 7.5

# jab aap chahate ho ki aap ka kaam one line m ho  jaye 
# jb function ko as a argumnt pass krte hai to lambda function use hota hai
def appl(fx,value):
    return 10+fx(value)

print(appl(cube,5)) # 135








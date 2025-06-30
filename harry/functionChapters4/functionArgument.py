# four types of argument 
# deafult argument 
# keayword argument 
# variable argumeent
# required argument

def average(a=9,b=1):
    print("the average is ",(a+b)/2)

def averageCOMPULSARYARGUMENT(a,b,c=1):
    print("the average is ",(a+b+c)/2)


average()
average(5)
average(4,6)
average(b=6)
average(b=6,a=21)# keyword argument 
averageCOMPULSARYARGUMENT(1,2,3)# required argument


def name(fname,mname="jhone",lname="whatsapp"):
    print("hello,",fname,mname,lname)

name("thakur","aditya","singh")

def average(*numbers):
    print(type(numbers))  # forming tuple
    sum=0
    for i in numbers:
        sum=sum+i
    print("the average is ",sum/len(numbers))

average(1,2,3,4,5,6,7,8,9)

def Greetingname(**name):
    print(type(name))
    print("hello,",name["fname"],name["mname"],name["lname"])

Greetingname(fname="thakur",mname="aditya",lname="singh")



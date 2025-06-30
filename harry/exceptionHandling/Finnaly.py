try:
    print()
except:
    print("")

try:
    l=[1,2,3,4,5]
    i=int(input("enter the index: "))
    print(l[i])
except:
    print("some error occurred")
finally:
    print("always excecuted irrespactive of error")



#
def func1():
    try:
        l=[1,2,3,4,5]
        i=int(input("enter the index: "))
        print(l[i])
        return 1
    except:
        print("some error occurred")
        return 0
    finally:
        print("will get executed even after return keyword is been used")


x=func1()
print(x)







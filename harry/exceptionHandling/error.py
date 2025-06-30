a=input("enter the number: ")
print(f"Multiplication table of {a} is: ")

for i in range(1,11):
    print(f"{int(a)}*{i}={int(a)*i}")

print("some important linke of code") # not will be printed in this case

# now how to handle this type error 
try:
    for i in range(1,11):
        print(f"{int(a)}*{i}={int(a)*i}")
except Exception as e:
    print(e)
    print("some error occured")
    print("invalid input")

print("some important linke of code") # not will be printed in this case



# multi try and catch block
try:
    num=int(input("enter any integer: "))
    a=[6,3]
    print(a[num])
except ValueError:
    print("number entered is not an integer. ")
except IndexError:
    print("invalid index")
# server error   






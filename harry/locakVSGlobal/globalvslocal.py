x=4
print(x)

def hello():
    x=10
    y=1
    print(f"the local x is {x}")
    print("hello harry")


print(f"the global x is {x}")
hello()
print(y) # will give an error because y is local and cant be accessed outside 
x=6
print(f"the global x is {x}")

















x=4
print(x)
def my_def():
    global x
    x=10
    y=1
    print(f"the local x is {x}")
    print(f"the local y is {y}")


print(f"the global x is {x}")
my_def()
print(y) # will give an error because y is local and cant be accessed outside 
x=6
print(f"the global x is {x}")
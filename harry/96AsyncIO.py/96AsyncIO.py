# asych io 
# na hi multithreddind and nahi hi multiprocessing 



import time
import asyncio
def function1():
    time.sleep(3)
    print("func1")

def function2():
    time.sleep(3)
    print("func2")

def function3():
    time.sleep(3)
    print("func3") 

function1() # if function 1 execute nahi hua to code ruk jayega orr bnd ho jayega 
function2() # if function 2 jb tk puri tarike sse nahi chala to pura code ruk jayega 
function3() # ek complete hoone ke baad dusri line chalegi 
# this is way of normal executaion of program 
# jab tk function 1 execute hoke khatam nahi ho jayega tb tk function1 follwed by function2 function 3 uske baad chalega 


# but isske api call hui to dikkat ho jayegi 
# to calling ka naya trika sahi ki by using async kewards 
# ki wo wali jitna time legi legi baki ko exexcute hone do 

async def function1():
    time.sleep(3)
    print("func1")

async def function2():
    time.sleep(3)
    print("func2")

async def function3():
    time.sleep(3) 
    print("func3") 


# they cant be called like this innko await key word de ke hi call kiya ja skta hai 
# nahi to nahi call kr skte hai 
    #function1()
    #function2()
    #function3() 
async def main():
    await function1()  # innko ek satth abhi bhi nahi chalaya ja skta 
    await function2()
    await function3()


#  the correct way to use async function in the python  is this 
async def main():
    task=asyncio.create_task(function1())
    await function2()
    await function3()

asyncio.run(main())
# sir ne bataya ki yaha pr ek accha organization nahi milta function ko chalane ka to issko use nahi krte hai issi jagah gether use krte hai organization ke liye 
# dusari baat ye ki jb function 1 ko time mil jayega  chalne ko to wo chal jayagag  
























































































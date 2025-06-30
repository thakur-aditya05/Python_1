# asych io 
# na hi multithreddind and nahi hi multiprocessing 



import time
import asyncio

async def function1():
    await asyncio.sleep(3)
    print("func1")
    return "harry"

async def function2():
    await asyncio.sleep(3)
    print("func1")
    return "harr"

async def function3():
    await asyncio.sleep(3)
    print("func1") 


# ye ab teeno function ek saath chalenge and inhe ab koi dikkat nahi hogi 
# all three function run paraellel chalenge 
async def main():
    L = await asyncio.gather(
        function1(),
        function2(),
        function3(),
    )
    print(L)






















































































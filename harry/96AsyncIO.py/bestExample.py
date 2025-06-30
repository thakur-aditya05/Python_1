# https://www.codementor.io/@aviaryan/downloading-files-from-urls-in-python-77q3bs0un

# for parallel execution 

import requests


import time
import asyncio

async def function1():
    url = 'http://google.com/favicon.ico'
    r = requests.get(url, allow_redirects=True)
    open('google1.ico', 'wb').write(r.content)
    print("func1") 


async def function2():
    url = 'http://google.com/favicon.ico'
    r = requests.get(url, allow_redirects=True)
    open('google2.ico', 'wb').write(r.content)
    print("func1")


async def function3():
    url = 'http://google.com/favicon.ico'
    r = requests.get(url, allow_redirects=True)
    open('google3.ico', 'wb').write(r.content)
    print("func1") 


# ye ab teeno function ek saath chalenge and inhe ab koi dikkat nahi hogi 
# all three function run paraellel chalenge 
# will will work together 
async def main():
    # ye await use krne pr ek ek kr ke chalenge ab ye dekhe lena jo ki dikkt dega 
    # orr await sync pair ka use krne ka sahi taria ye hhai 
    await function1()
    await function2()
    await function3()
    return 3
    # orr await sync pair ka use krne ka sahi taria ye hhai
    # L = await asyncio.gather(
    #     function1(),
    #     function2(),
    #     function3(),
    # )

    # print(L)
async def main():
    # await function1()
    # await function2()
    # await function3()
    # return 3
    # orr await sync pair ka use krne ka sahi taria ye hhai
    L = await asyncio.gather(
        function1(),
        function2(),
        function3(),
    )

    print(L)
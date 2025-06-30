# concurrent.feature-launching 

# 500 url ka dounload krne ke liye ek saath wo bhi issko use krna hai 

import threading
import time 
# concurrrent importing 
from concurrent.futures import ThreadPoolExecutor


# indicate some task being done 
def func(seconds):
    print(f"Sleepig for {seconds} seconds")
    time.sleep(seconds)
    return seconds

def poolingDemo():
    with ThreadPoolExecutor() as executor:
        l=[2,3,4,5]
        results=executor.map(func,l)
        for result in results:
            print(result)

poolingDemo()
















































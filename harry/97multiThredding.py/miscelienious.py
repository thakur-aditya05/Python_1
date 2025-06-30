# concurrent.feature-launching 

import threading
import time 
# concurrrent importing 
from concurrent.futures import ThreadPoolExecutor


# indicate some task being done 
def func(seconds):
    print(f"Sleepig for {seconds} seconds")
    time.sleep(seconds)

time5=time.perf_counter()
#same code using threds 
t1=threading.Thread(target=func,args=[4])
t2=threading.Thread(target=func,args=[1])
t3=threading.Thread(target=func,args=[2])


t1.start() # bg me ye process start ho gayi hai 
t2.start() # bg me ye process start karo and aage badho 
t3.start() # bg me start kaaro and aage badho 

t1.join() # bg me ye process start ho gayi thi or ab khatam hone ka wait karo isske  
t2.join() # bg me ye process start ho gayi thi or ab khatam hone ka wait karo isske   
t3.join() # bg me ye process start ho gayi thi or ab khatam hone ka wait karo isske  



time6=time.perf_counter()
print(time6-time5)





# jub bulk me koi kaam krni ho to ye pooling demo kaam aata hai 
def poolingDemo():
    with ThreadPoolExecutor(max_workers=1) as executor:
        future=executor.submit(func,3)  # func function ka use krna chahta hu and want to sleep for 3 sec 
        print(future.result())
        future=executor.submit(func,2)  # func function ka use krna chahta hu and want to sleep for 3 sec 
        print(future.result())
        future=executor.submit(func,1)  # func function ka use krna chahta hu and want to sleep for 3 sec 
        print(future.result())
poolingDemo()

# ek baar issko run krke deko 
# jub bulk me koi kaam krni ho to ye pooling demo kaam aata hai 
def poolingDemo():
    with ThreadPoolExecutor(max_workers=1) as executor:
        # ye sb 4 sec me execute ho jayneg
        future1=executor.submit(func,3)  # func function ka use krna chahta hu and want to sleep for 3 sec 
        future2=executor.submit(func,2)  # func function ka use krna chahta hu and want to sleep for 3 sec 
        future3=executor.submit(func,1)  # func function ka use krna chahta hu and want to sleep for 3 sec 
        # orr ye none printing ho jayegi 
        print(future1.result())
        print(future2.result())
        print(future3.result())
poolingDemo()
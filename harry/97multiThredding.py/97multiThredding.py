import threading
import time

#  multi tasking means ek saath khana bananan and serve krna 



# indicate some task being done 
def func(seconds):
    print(f"Sleepig for {seconds} seconds")
    time.sleep(seconds)

time1=time.perf_counter()
#normal way of running code 
func(4)
func(1)
func(2)
time2=time.perf_counter()
print(time2-time1)









# indicate some task being done 
def func(seconds):
    print(f"Sleepig for {seconds} seconds")
    time.sleep(seconds)


time3=time.perf_counter()
#same code using threds 
t1=threading.Thread(target=func,args=[4])
t2=threading.Thread(target=func,args=[1])
t3=threading.Thread(target=func,args=[2])


t1.start() # bg me ye process start ho gayi hai 
t2.start() # bg me ye process start karo and aage badho 
t3.start() # bg me start kaaro and aage badho 

time4=time.perf_counter()
print(time4-time3)









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
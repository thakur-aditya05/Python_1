# type of dp in this 
# kind of memoization kr leta hai yani wo ceezon ko yaad kr leta hai ki aise hi kaam karrega 
# jaise kisi karan ke liye 2 ki liye value 4 calculate ho gayi hai to wo store kr lega ki 2 ki value 4 hai 

# jb jb recomputational hoga values ka tb tb ye wala concept use krna hai nahia to nahi use krna hai
# bahut bahut limited hai values haii wo repeat kr rahi hai N


from functools import lru_cache
import time 

@lru_cache(maxsize=None)
def fx(n):
    time.sleep(5)
    return n*5

# memoization hota hao 
print(fx(20)) #ye 20 ki vaue ko stoore kr lega and recomputatin se baccha lega 
print("done for 20")
print(fx(10)) #ye 10 ki vaue ko stoore kr lega and recomputatin se baccha lega 
print("done for 10")
print(fx(40))  #ye 40 ki vaue ko stoore kr lega and recomputatin se baccha lega 
print("done for 40")

# re computational
print(fx(20)) #ye 20 ki vaue ko stoore kr lega and recomputatin se baccha lega 
print("done for 20")
print(fx(10)) #ye 10 ki vaue ko stoore kr lega and recomputatin se baccha lega 
print("done for 10")
print(fx(40))  #ye 40 ki vaue ko stoore kr lega and recomputatin se baccha lega 
print("done for 40")








# memoization ---> 

from functools import lru_cache
@lru_cache(maxsize=None)
def fib(n):
    if n<2:
        return n
    return fib(n-1)+fib(n-2)
print(fib(20))

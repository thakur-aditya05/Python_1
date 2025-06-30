# timemodule 
# for vs while ki speed depanding on cpu weight 

# https://pypdf2.readthedocs.io/en/3.0.0/user/merging-pdfs.html
# https://docs.python.org/3/library/time.html



import time
def usingWhile():
    i=0
    while i<5000:
        i=i+1
        print(i)
def usingFor():
    for i in range(5000):
        print(i)
init=time.time()
usingFor()
t1=time.time()-init # for ko kitna time laga chalne ke liye 

init=time.time()
usingWhile()
t2=time.time()-init

print(f"t1={t1} and t2={t2}")





























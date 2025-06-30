# shuttile module 


# 100 folder me 100 files ----> brings back them to one folder 
# pip install 
# https://docs.python.org/3/library/shutil.html#module-shutil


# shutil.copy(src,dst)
import shutil 
shutil.copy("main.py","main2.py")



#shutil.copy2(src,dest)

#
#shutil.copytree(src,dest) # pura folfder copy kr lega 



#shutil.move(src,dest) # pura file ko ek locaton se dusare location me move krne ka kaam krti hai 
shutil.move(".tutorial/file.file","file.file")




#shutil.rmtree(path) # pura folfder ya file  delete kr dega 
shutil.rmtree("mytuturial")
shutil.rmtree("mytuturial")  # Deletes the folder named "mytuturial" along with its contents
os.remove("file.file")
 











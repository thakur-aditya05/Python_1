with open("demo.txt","r") as f: # complete path dena padta hai jb same folder me nahi hoti hai 
    # as ---> alias name hota hai 
    data = f.read()
    print(data)
    print(type(data)) # data type string hota hai
# with syntax me file ko close karne ki jarurat nahi hoti hai wo aumtomatic close ho jati hai









# Error in the code!
# The file is still in write mode (w+), and after writing, the cursor is at the end of the file.
# f.read() tries to read from the current cursor position (end of the file), so it returns an empty string.
# To fix this: Move the cursor back to the beginning using f.seek(0) before f.read().
with open("demo.txt","w+") as f:  # file ko truncate kr kr open karega and cursor at [0][0]
    f.write("hello") # hello (link dega in file )(cursor end me hoga hello ke )
    f.write("world") #  world (lkh dega in file ) and cursor end me hoga world ke
    f.
    f.write("python") 
    f.write("java")
    data = f.read()
    print(data)
    print("write operation    done")










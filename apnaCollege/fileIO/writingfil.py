f=open("demo.txt","w") # complete path dena padta hai jb same folder me nahi hoti hai
f.write("keval w ko use krne pr data overide ho jata hai puri traike se ") # write function se file me data write ho jata hai
f.close() # file ko close karna jaruri hai

f=open("demo.txt","a") # complete path dena padta hai jb same folder me nahi hoti hai
f.write("keval a ko use krne pr data next line se start ho jayega ") # write function se file me data write ho jata hai
f.close() # file ko close karna jaruri hai


# kevval w and a mode kholne pr file create ho jati hai agar file nahi hoti hai ussi naam ki to
f=open("noname.txt","w") # complete path dena padta hai jb same folder me nahi hoti hai


# stack overflow  for impormation 

# r+==> read and write  and file pointer at the begining of the file i.e jitna writing ke liye argument bhejenge na utna override kr jayega 
f=open("demo.txt","r+") 
f.write("strating ke n char overide  kr dega ") # write function se file me data write ho jata hai
f.close() # file ko close karna jaruri hai






# w+==> read and write  and file puri truncate hoke open hogi and file pointer at the begining of the file i.e jitna writing ke liye argument bhejenge na utna override kr jayega
f=open("demo.txt","w+")
print(f.read()) # puri file truncated hoke open hogi yani sara data erase ho jayega
f.write("strating se likhi jayegi  ") # write function se file me data write ho jata hai
f.close() # file ko close karna jaruri hai










# a+==> read and write  
f=open("demo.txt","a+") # cursor end me chalajayega 
print(f.read()) # cursor last me hone ke karan kuch bhi nahi print hoga 
f.write("end me likha jayega ") # write function se file me data write ho jata hai but iss baar end me add hoga kyo ki cursor end me hai and wo a+ ke karan hua hai 
f.close() # file ko close karna jaruri hai
 










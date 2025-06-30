f=open("demo.txt","r") # complete path dena padta hai jb same folder me nahi hoti hai
data = f.read() # read function se file ka data read ho jata hai and wo bhi string format  me  hota hai
print(data) # read function se file ka data read ho jata hai 
print(type(data)) # data type string hota hai
f.close() # file ko close karna jaruri hai
'r'
'w'
'a'
'rt'
'x'
'rb'
'wb'
'ab'
"+"    
data = f.read(5) # starting 5 characters read karne ke liye
print(data)


line1 =f.readline() # read line by line
print(line1)


# issme cursor imagine krna padtda jo ki initially file ko open krte samay  [0][0] pe hota hai
# jab read function call hota hai to cursor right side me move hota hai and at the end me  cursor file ke end me hota hai
# close and open karo to fir wo starting me pahuch jata hai no matter kaha pe chhora gaya tha 










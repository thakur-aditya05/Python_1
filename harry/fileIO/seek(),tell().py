# alag folder hai isska bhai dont waste time for that 


# seek() is used to move the cursor to a particular position in the file
with open('file.txt','r') as f:
    print(type(f))
    #move to the 10th byte in the file.txt 
    f.seek(10)
    
    #read the next 5 bytes
    data=f.read(5)# read next 5 bytes from  10th byte
    print(data)
 





# tell() is used to get the current position of the cursor in the file
with open('file.txt','r') as f:
    print(type(f))
    #move to the 10th byte in the file.txt 
    f.seek(10)
    
    #read the next 5 bytes
    
    data=f.read(5)# read next 5 bytes from  10th byte
    print(f.tell())# tell() will return the current position of the cursor in thr file 
    print(data)





# truncate 
with open ('file2.txt','w') as f:
    f.write('Hello World') # write 11 bytes "hello world" in the file2.txt
    f.truncate(5) #will delete all the bytes or char affter 5th byte 
    print(f.read()) # cursur ke baad 







# create new file in "fileExperiment" filder
# write the few lunes of code there only 

# READING OF FILE#this will help to read the file 
f=open('myfile.txt','r')
print(f)
text=f.read()
print(text)
f.close()





#WRITING THE FILE  # this will overide  the file 
f=open('myfile.txt','w')
f.write('hello world')
f.close()


# READING OF FILE #this will help to read the file 
f=open('myfile.txt','r')
print(f)
text=f.read()
print(text)
f.close()



#APPEND THE FILE  # this will append the file 
f=open('myfile.txt','a')
f.write('  hello world throw append ')
f.close()


# READING OF FILE #this will help to read the file 
f=open('myfile.txt','r')
print(f)
text=f.read()
print(text)
f.close()



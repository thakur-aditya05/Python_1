# create new file in "fileExperiment" filder
# write the few lunes of code there only 

# READING OF FILE
f=open('myfile.txt','r')
print(f)
text=f.read()
print(text)
f.close()





#WRITING THE FILE 
f=open('myfile.txt','w')
f.write('hello world')
f.close()



#APPEND THE FILE 
f=open('myfile.txt','a')
f.write('hello world throw append ')
f.close()



with open('myfile.txt','a'):
    f.write('hello word under with key word and appending   ')





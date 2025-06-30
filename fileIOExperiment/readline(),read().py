f=open('myfile0.txt','r')
while True:
    line=f.readline()
    
    if not line:
        break
    
    print(line)




f=open("myfile2.txt",'r')
i=0
while True:
    i=i+1
    line=f.readline()
    if not line:
        break
    m1=line.split(",")[0]
    m2=line.split(",")[1]
    m3=line.split(",")[2]
    print(f"Marks of student {i} in Maths is : {m1}")
    print(f"Marks of student {i} in Maths is : {m2}")
    print(f"Marks of student {i} in Maths is : {m3}")
    print(line)


# above all are string based operation 
f=open("myfile2.txt",'r')
i=0
while True:
    i=i+1
    line=f.readline()
    if not line:
        break
    m1=int(line.split(",")[0])
    m2=int(line.split(",")[1])
    m3=int(line.split(",")[2])
    print(f"Marks of student {i} in Maths is : {m1*2}")
    print(f"Marks of student {i} in Maths is : {m2*2}")
    print(f"Marks of student {i} in Maths is : {m3*2}")
    print(line)




# this will create new file and write these lines and also if file existx then simply add new file 
f=open('myfile3.txt','w')
lines=['line 1\n','line 2\n','line 3\n']
f.writelines(lines)
f.close()

# or for doing same work 
f=open('myfile3.txt','w')
lines=['line 1','line 2','line 3' ,'line 4', 'line 5']
for line in lines:
    f.write(line+'\n')
f.close()
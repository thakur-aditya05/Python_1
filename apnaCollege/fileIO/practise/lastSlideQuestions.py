count=0

with open("numerical",'r') as f:
    data=f.read()
    print(data)
    
    
    # basic code to get numbers 
    num=""
    for i in range(len(data)):
        if(data[i]==","):
            print(int(num))
            num=""
        else:
            num+=data[i]
    
    # advanced code to get numbers
    nums=data.split(",") # number ko split kr diya comma ke basis pr 
    for val in nums :
        if(int(val%2==0)):
            print(val)
            count+=1

print(count)

    
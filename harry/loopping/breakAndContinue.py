for i in range(12):
    if(i==10):
        print("skip the iteration"+ " no printing of table 10 will happen ")
        continue
    print("5*",i,"=",5*i)
else:
    print("we ended for loop")
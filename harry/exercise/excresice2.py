import time 
t=time.strfttime('%H:%M:%S')
hour=int(time.strftime('%H'))
print('Current time is:',t)


if(hour>0 and hour<12):
    print('Good Morning')
elif(hour>=12 and hour<17):
    priint(good )
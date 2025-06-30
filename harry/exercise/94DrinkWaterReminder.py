# drink water reminder 
# voice note 
# email ke through 
# exercise 11 DDrink water reminder 
# write a python program which remind you of drinking every two hours 
# beep sound orr should send a notification on google 


# search it on google and run in commond prompt ----> window display notification 
import os
command= " osascript -e \'say \"herry drink water\"\'; osascript -e \'display alert \"herry drink water\" \' "
os.system(command)







import os
import time

REPEAT_INTERVAL=3600 #Repeate frequency in seconde

while True: # dont use while true(# Windows  task shedular ) or (cron jobs)
    command= " osascript -e \'say \"herry drink water\"\'; osascript -e \'display alert \"herry drink water\" \' "
    os.system(command)
    time.sleep(REPEAT_INTERVAL)





# for windows 
import time 
from  plyer import notification
time_hour=float(input("time after which u  will drink water "))
while True:
    time.sleep(3600*time_hour)
    notification.notify(title="water", message="drink water ",timeout=2)




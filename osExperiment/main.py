import os

# os.mkdir("data") # 
if(not os.path.exists("data")):
    os.mkdir("data")

for i in range(0,100):
    os.mkdir(f"data/Data{i+1}")















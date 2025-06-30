import os 
folders =os.listdir("data")

# print(folders)

# for folder in folders:
#     print(folder)



for folder in folders:
    print(os.listdir(f"data/{folder}"))

print(os.getcwd())  # print current working directry 
os.chdir("/main")  # it will change the working directory  but nahi krna hai ye 
print(os.getcwd())  # print current working directry 




# ab khud se explore karo 
# os. 
# os.system
# os.delete 
 

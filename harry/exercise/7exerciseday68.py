# Write a program to clear the clutter inside a folder on your computer. 
# You should use os module to rename all the png images from 1.png all the
# way till n.png where n is the number of png files in that folder. 
# Do the same for other file formats 
# for example if u have name png like 

# ye function bana ke krna hai aise naki kisi orr tarike se that is if .png if passed to sari png file rename ho jaye 

# sfdsf.png --> 1.png
# vfsf.png --> 2.png
# this.png --> 3.png
# design.png --> 4.png
# name.png-->5.png




# pngegg.com  #good website to download 
# os.listdir("folder ka naam likhna hai jiske under fiile ho jaise 'Clustred folder '") # ye function list kr dega saare folder jo ki clusteredFolder ke under honge 
# os.rename("clutteredFolder/file.txt","clutteredFolder/6.txt") # file ko rename kr dega uss clustered folder ke under wale 

import os

files=os.listdir("clutteredFolder")
i=1
for file in files:
    if file.endswith(".png"):
        print(file)
        os.rename(f"clutteredFolder/{file}",f"clutteredFolder/{i}.png")
        i=i+1















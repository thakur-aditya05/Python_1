# write a python program to circulate a message into secrate code language. use the rules below
# to translate normal english into secrate code language 

# tanslate normal English into secret code language

# coding:
# if the word contains atleast 3 characters, remove the first letter and append it at the end 
# now append three random characters at the starting and the end 
# else:
# simply reverse the string

# Decoding:
# if the word contains less than 3 characters, reverse it
# else:
# remove 3 random characters from start and end. Now remove the last letter and append it to he beginning

# Your program should ask whether you want to code or decode



# 
# string ko cut karo and then append karo bs 













# goes fo random module for randome number 
# solutions

st=input("enter message:  ") # input lega users se 
words=st.split(" ") #jo bhi gaps honge waha se split kr dega 
coding=input(" 1 for coding or 0 for decoding ")
coding=True if (coding=="1") else False
print(coding)
if(coding):
    nwords=[] #
    for word in words:
        if(len(word)>=3):
            r1="dcf"
            r2="d32"
            stnew=r1+word[1:]+word[0]+r2
            nwords.append(stnew)
        else:
            nwords.append(word[::-1])
    print(" ".join(nwords))
else:
    nwords=[] #
    for word in words:
        if(len(word)>=3):
            stnew=word[3:-3]
            stnew=stnew[-1]+stnew[:-1]
            nwords.append(stnew)
        else:
            nwords.append(words[::-1])
    print(" ".join(nwords))







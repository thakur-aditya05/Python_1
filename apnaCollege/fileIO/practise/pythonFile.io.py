with open('practice.txt','w') as f:
    f.write('')
    f.write('')
    f.write('')
    f.write('')
    f.write('')



with open('practice.txt','r') as f: #`r` mode me open karega
    data=f.read() #data variable me file ka data store ho jayega
new_data=data.replace('java','python') # as data is of kind string that is why all this happened  replace function se data me se java ko python me replace kar diya
print(new_data)
with open('practice.txt','w') as f: #`w` mode me open karega
    f.write(new_data) #new_data ko file me write kar dega


def check_for_word():
    word='learning'
    with open("practice.txt",'r') as f:
        data=f.read()
        if(data.find(word)!=-1):
            print(f"{word} is present in the file")
        else:
            print(f"{word} is not present in the file")

check_for_word()
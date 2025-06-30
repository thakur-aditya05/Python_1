def checkForLine():
    word="learning"
    data=True
    lineNo=1
    with open("practice.txt","r") as f:
        while data:
            data=f.readline()
            if(word in data):
                print(f"{word} is present in line {lineNo}")
                return
            lineNo+=1 # compalsaory hai chalna 
        print(f"{word} is not present in the file")


check_for_line()





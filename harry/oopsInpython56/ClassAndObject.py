class Person: # this is class of person 
    name="aditya"
    ocuupation="student"
    netWorth=10
    

a=Person() # this is object of name a
print(a.name,a.occupation) # aditya student(by default set kr rakhe hai)
a.name="aman"  #name change kr diya
a.occupation="developer" #occupation change kr diya
print(a.name,a.occupation)  # aman developer




class Person: # this is class of person
    name="aditya"
    ocuupation="student"
    netWorth=10
    def info(self):
        print(f"Name:{self.name}\nOccupation:{self.occupation}\nNetWorth:{self.netWorth}")

b=Person() # this is object of name b
b.info() # Name:aditya


# self===>object ko refer krta hai 
# jaie b.info kiya to self===>b  class ke under self ki
# jaie a.info kiya to self===>a

c=Person() # this is object of name c --> c ek object banni 
c.name="nikita" #name change kr diya --> 
c.ocuupation="doctor" #occupation change kr diya
c.netWorth=100 #netWorth change kr diya
c.info() # Name:nikita

d=Person() # this is object of name d having deafulat value as aditya student 10













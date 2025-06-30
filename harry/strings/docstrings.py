# comment ko change krne ke baad prograam change nahi hoga
#but doc string ko change krne ke baad program change hoga 
# doc string kuch information deti hai function ke bare me and wo doc variable me store hoti hai
# and usko print karne ke liye hum __doc__ use karte hai
#doc string right below jati hai function ke and uske liye hum triple quotes use karte hai (ALWASYS)

def square(n):
    ''' this functions returns the square of the number'''
    return n**2

square(4)
print(square.__doc__) # this will print the doc string of the function



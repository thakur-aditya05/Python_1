letter ="hey my name is {} and i am from {}"

country="india"
name="sachin"

print(letter.format(country,name))
# more improved way
letter ="hey my name is {1} and i am from {0}"

country="india"
name="sachin"

print(letter.format(country,name))
# new technology 

country="india"
name="sachin"
letter =f"hey my name is {name} and i am from {country}"
print(letter)
# this is absolutly new 
# this is called f-string
# this is the most improved way to print the string


price=48.294949
txt=f"the price is {price:.2f} dollars"
print(txt)
print(txt.format())
print(type(txt))




letter =f"hey my name is {{name}} and i am from {{country}}"
print(letter)

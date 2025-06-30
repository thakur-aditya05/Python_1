
from functools import reduce 

# print summation of all object 
summation=lambda a,b:a+b
numbers = [3, 4, 6, 9, 34, 12]
sum=reduce(summation,numbers) # 3+4=7+6=13+9=22+34=56+12=68
print(sum) # 68
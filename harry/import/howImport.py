import math
result= math.sqrt(9)
print(result)

from math import sqrt, pi
result= sqrt(9)*pi
print(result)



from math import pi,sqrt as s
result=s(9)*pi
print(result)

from math import pi,sqrt as s
result=s(9)*pi
print(result)


import math as mh
result=mh.sqrt(9)*mh.pi
print(result)

print(dir(mh)) # kon kon se function hai 
print(mh.__doc__ , type(mh.__doc__))
print(mh.__loader__,type(mh.__loader__))
print(mh.isfinite,type(mh.nan))

# 
# 
from aditya import *
from aditya import welcome,aditya
welcome()
print(aditya)

import aditya as ad
ad.welcome()
print(aditya)



























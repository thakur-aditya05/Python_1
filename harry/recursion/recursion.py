# factorial(7)= 7*6*5*4*3*2*1=5040
# factorial(5)= 5*4*3*2*1=120
# factorial(1)= 1
# factorial(0)= 1
#factorial(n)=n*factorial(n-1)

def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n*factorial(n-1)

def factorial(n):
    if(n==0 or n==1):
        return 1
    return n*factorial(n-1)

print(factorial(7))
print(factorial(5))


# write teh for fibonaci series
# 0 1 1 2 3 5 8 13 21 34 55 89 144
# fib(n)=fib(n-1)+fib(n-2) this is home work 
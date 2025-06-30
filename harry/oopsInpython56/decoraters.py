def hello():
    print('Hello')
hello()
# output: Hello
# before the run it says good morning 


def greet(fx):
    def mfx():
        print('Good Morning')
        fx()
        print('THANK YOU FOR CALLING THIS FUNCTION')
    return mfx

@greet # this is a decorator jo ki hello function ko modify kr dega yani saga raha hai 
def hello():
    print('Hello')

hello()
greet(hello)() # ya to  ye kr do greet(hello)()  ya to @ greet kr do



def add(a,b):
    print(a+b)


# for those function which are taking argument
def greetForArgument(fx):
    def mfx(*args,**kwargs):
        print('Good Morning')
        fx(*args,**kwargs)
        print('THANK YOU FOR CALLING THIS FUNCTION')
    return mfx

greetForArgument(add)(5,6) # Good Morning 11 THANK YOU FOR CALLING THIS FUNCTION

















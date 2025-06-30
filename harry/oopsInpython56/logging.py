import logging 

def log_function_call(func):
    def decorated(*args, **kwargs):
        logging.info(f'calling {func.__name__} called with args {args} and kwargs {kwargs}')
        result=func(*args, **kwargs)
        logging.info(f'{func.__name__} returned {result}')
        return result
    return decorated


@log_function_call
def add(a,b):
    print(a+b)


add(5,6)
# output: 11

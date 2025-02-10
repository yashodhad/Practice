# Decorators with Arguments

# Sometimes, you may need to pass arguments to the decorated function. you can do this by defining * args and **kwargs in the wrapper function.

def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before the funtion call")
        result = func(*args, **kwargs)
        print("after the function call")
        return result
    return wrapper

@my_decorator
def say_hello(name):
    print(f"Hello,{name}")

# using the decorator function
say_hello('Alice')
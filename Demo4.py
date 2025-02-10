# using multiple decorators

# you can apply multiple decorators to a single functon by stacking them
def decorator1(func):
    def wrapper(*args, **kwargs):
        print("Decorator 1")
        return func(*args, **kwargs)
    return wrapper

def decorator2(func):
    def wrapper(*args, **kwargs):
        print("Decorator 2")
        return func(*args, **kwargs)
    return wrapper

@decorator1
@decorator2
def say_hello(name):
    print(f"hello:{name}!")

# using the decorator function


say_hello("yashodha")
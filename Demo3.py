# Decorators functions with Return values

#  If the function being decorated return a value, the decorator should return that value as well

def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before the funtion call")
        result = func(*args, **kwargs)
        print("after the function call")
        return result
    return wrapper

@my_decorator
def add(a, b):
    return a + b

# using the decorator function
result = add(3, 4)
print(f"Result : {result}")
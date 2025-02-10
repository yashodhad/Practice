#  A decorator is a function that takes another function as an argument and extends its behavior without modifying it.

# simple example
# after commit the file, just test
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called")
        func()
        print("Something is happening after the function is called")
    return wrapper  # Return the wrapper function itself, not the result of calling it


@my_decorator
def say_hello():
    print("Hello!")

# using the decorator function
say_hello()



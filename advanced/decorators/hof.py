# Note: work on del and delete operators in Python and JS

# HOF: higher Order Function: It's a function that either accepts a function as input or return a function as output
def greet(func):
    func()

def greet2():
    def func():
        pass

    return func

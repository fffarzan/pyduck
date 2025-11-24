# HOF with a function as an input
def greet(func):
    func()

# HOF with a function as an output
def greet2():
    def func():
        pass

    return func

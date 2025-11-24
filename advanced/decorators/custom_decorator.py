def my_dec(func):
    def wrap_func():
        print('***************')
        func()
    
    return wrap_func

@my_dec
def hello():
    print('hellooo')

hello()

# Decorators is like of these calls:
my_dec(hello())
my_dec(hello)()

def my_other_dec(func):
    def wrap_func(*args, **kwargs):
        print('***************')
        func(*args, **kwargs)

    return wrap_func

@my_other_dec
def my_other_hello(greeting, emoji=':)'):
    print(greeting, emoji)

my_other_hello('Hiiii')

# say_hello() # this will give an error. there is no hoisting here!

def say_hello():
    print('my hello')

say_hello()

print(say_hello) # show the place of the function in the memory
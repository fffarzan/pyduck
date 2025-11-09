# say_hello() # this will give an error. there is no hoisting here!

# with default parameter
def say_hello(name='jedi', emoji='=)'): # parameter
    print(f'my hello {name}, {emoji}')

print(say_hello) # show the place of the function in the memory

say_hello()

# positional arguments (matters where we put the arg)
say_hello('fffarzan', ':)') 

# keyowrd arguments
say_hello(emoji=':)', name='fffarzan')
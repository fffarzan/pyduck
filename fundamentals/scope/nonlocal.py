def outer():
    x = 'local'

    def inner():
        nonlocal x # go and come the parent x var to the inner function. like closure.
        x = 'nonlocal'
        print('inner:', x)
    
    inner()
    print('outer:', x)

outer()
def super_func(*args, **kwargs): # *args for numbers
    print(args) # tuple of arguments
    print(kwargs) # a dictionary
    
    total = 0
    for items in kwargs.values():
        total += items

    return sum(args) + total

print(super_func(1, 2, 3, 4, 5, num1=5, num2=10))

# RULE: in order: params, *args, default params, **kwargs
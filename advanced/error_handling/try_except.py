# Error handling allows us running the script even if there is an error in it.

def sum(num1, num2):
    try:
        return num1 + num2
    except TypeError as err:
        print(err)

print(sum(1, '2'))

def divide(num1, num2):
    try:
        return num1 / num2
    except (TypeError, ZeroDivisionError) as error:
        print(error)

print(divide(1, 0))



while True:
    try:
        age =  int(input('What\'s your age?'))
        10 / age
        # raise ValueError('cut it out ') # raising a value error and it goes to ValueError except
        # raise Exception('I said cut it out!')
    except ValueError:
        print('please enter a number')
        continue # like continue in for loop, goes back to the top
    except ZeroDivisionError:
        print('please enter an age highet than 0')
        break # like break in for loop, breaks the while loop
    else: # this will be done just after try
        print('thanks')
        # break # it totaly derives out the last print line!
    finally: # this will be done after try or excepts
        print('finally!!')

    print('Can you hear me?!')

import utility

print(utility)
print(utility.multiply(2, 3))
print(type(utility.st)) # result: <class 'utility.Student'> --> comes from utility module!



import shopping.shopping_cart
from shopping.shopping_cart import buy
from shopping import shopping_cart

print(shopping.shopping_cart)
print(shopping.shopping_cart.buy('apple'))
print(buy('banana'))
print(shopping_cart.buy('berry'))



if __name__ == '__main__': # this tells that if we are in the main file, run the code. 
    print('please run this')



from random import random, randint, choice, shuffle

print(random())
print(randint(1, 10))
print(choice([1, 2, 3, 4, 5]))
my_list = [1, 2, 3, 4, 5]
shuffle(my_list)
print(my_list)



# import sys

# filename = sys.argv[0]
# first_arg = sys.argv[1]

# print(f'first: {filename}, last: {first_arg}')

from pyjokes import get_joke

joke = print(get_joke())
print(joke)






# useful modules:
from collections import Counter, defaultdict, OrderedDict

list = [1, 2, 3, 4, 5, 6, 7, 7]
print(Counter(list)) # this is an algorithm question!
dict = defaultdict(lambda: 'does not exist', { 'a': 1, 'b': 2 }) # handles not found error
print(dict['a'])
print(dict['c'])
d1 = OrderedDict()
d1['a'] = 1 
d1['b'] = 2
d2 = OrderedDict()
d2['b'] = 2
d2['a'] = 1  
print(d1 == d2) # returns false because of order.

from datetime import time, date

print(time(5, 45, 2))
print(date.today())

from array import array

arr = array('i', [1, 2, 3]) # more performant than a list
print(arr[0])

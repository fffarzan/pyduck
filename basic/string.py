# Strings are immutable

# escape sequence
# \t : adds a tab.
# \n : new line.

long_string = '''
WOW
O O
---
'''
print(long_string)

# casting
# print('hello' + 5) # gives error
print(type(str(5)))

# formatted strings
name = 'Johnny'
age = 55
print(f'hi {name}. You are {age} years old.') # with f
print('hi {}. You are {} years old.'.format(name, age)) # old version
print('hi {1}. You are {0} years old.'.format(age, name)) # changing order
print('hi {new_name}. You are {age} years old.'.format(new_name='Sally', age=100)) # assigning new vars

# string indexes slicing
selfish = 'me me me'
print(selfish[:5])
print(selfish[0:6:2]) #[start:stop:stepover]
print(selfish[::2])
print(selfish[-1]) # start from the end
print(selfish[::-1]) # reverse
print(selfish[::-2])

# built-in methods
qoute = 'to be or not to be'
print(qoute.upper())
print(qoute.capitalize())
print(qoute.find('be')) # return that index of starting point
print(qoute.replace('be', 'me')) # creating a whole new string
print(qoute)
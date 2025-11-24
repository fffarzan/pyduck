# list: a form of array
# lists are mutable
# lists are passed by value, just like objects in JS.

li = [1, 2.5, 'a', True]
print(li[0:2]) # creates new list

basket = [1, 2, 3, 4, 5]
print(len(basket))

# adding to list
basket.append(7) # everything in python is an object. append does not create a copy of the list
print(basket)
basket.insert(4, 100)
print(basket)
basket.extend([101, 102])
print(basket)

# removing from list
basket.pop()
print(basket)
popped_item = basket.pop(0) # index that we wanna remove 
print(popped_item)
print(basket)
basket.remove(4) # value that we wanna remove 
print(basket)
basket.clear()
print(basket)

# walking
basket2 = ['a', 'b', 'c', 'd', 'e', 'd']
print(basket2.index('d'))
print(basket2.index('d', 0, 4))
print('d' in basket2)
print(basket2.count('d'))

# sort
basket3 = ['a', 'e', 'c', 'b', 'd']
print(sorted(basket3))
basket3.sort()
print(basket3)

# copy
new_basket3 = basket3[:] # copies the list
print(new_basket3)
new2_basket3 = new_basket3.copy()
print(new2_basket3)

# reverse
basket4 = ['a', 'e', 'c', 'b', 'd']
basket4.reverse()
print(basket4)

# range & list
print(range(1, 100))
print(list(range(1, 100)))

# join
my_sentence = ' '.join(['hi', 'bye'])
print(my_sentence)

# unpacking
a,b,c, *other, d = [1, 2, 3, 4, 5, 6, 7]
print(a, b, c, other, d)

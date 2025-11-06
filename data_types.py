# list: a form of array
# lists are mutable
# lists are passed by value, just like objects in JS.
# li = [1, 2.5, 'a', True]
# print(li[0:2]) # creates new list

# basket = [1, 2, 3, 4, 5]
# print(len(basket))

# # adding to list
# basket.append(7) # everything in python is an object. append does not create a copy of the list
# print(basket)
# basket.insert(4, 100)
# print(basket)
# basket.extend([101, 102])
# print(basket)

# # removing from list
# basket.pop()
# print(basket)
# popped_item = basket.pop(0) # index that we wanna remove 
# print(popped_item)
# print(basket)
# basket.remove(4) # value that we wanna remove 
# print(basket)
# basket.clear()
# print(basket)

# basket2 = ['a', 'b', 'c', 'd', 'e', 'd']
# print(basket2.index('d'))
# print(basket2.index('d', 0, 4))
# print('d' in basket2)
# print(basket2.count('d'))

# basket3 = ['a', 'e', 'c', 'b', 'd']
# print(sorted(basket3))
# basket3.sort()
# print(basket3)
# new_basket3 = basket3[:] # copies the list
# print(new_basket3)
# new2_basket3 = new_basket3.copy()
# print(new2_basket3)

# basket4 = ['a', 'e', 'c', 'b', 'd']
# basket4.reverse()
# print(basket4)

# range and list
# print(range(1, 100))
# print(list(range(1, 100)))

# my_sentence = ' '.join(['hi', 'bye'])
# print(my_sentence)

# list unpacking
# a,b,c, *other, d = [1, 2, 3, 4, 5, 6, 7]
# print(a, b, c, other, d)






# dictionary
# dictionary keys should be immutable
# dictionary = [{
#     'a': [1, 2],
#     'b': 'hi',
#     'c': True
# }]
# user = {
#     'basket': [1, 2, 3]
# }
# print(dictionary[0]['a'])
# print(user.get('c', 666)) # 666 is the default value

# user2 = dict(name='John')
# print(user2)
# print('name' in user2.keys())
# print('John' in user2.values())
# print(user.items())
# user3 = user2.copy()
# user3.update({ 'name': 'fffarzan' })
# print(user3)

# print(user2.popitem()) # randomly pops sth!
# print(user2.pop('name'))
# print(user2.clear())
# print(user3)




# dictionary keys should be immutable

dictionary = [{
    'a': [1, 2],
    'b': 'hi',
    'c': True
}]
user = {
    'basket': [1, 2, 3]
}
print(dictionary[0]['a'])
print(user.get('c', 666)) # 666 is the default value
print(user.items()) # getting all key-values

user2 = dict(name='John')
print(user2)
print('name' in user2.keys())
print('John' in user2.values())
print(user2.popitem()) # randomly pops sth!
print(user2.pop('name'))


# copying and updating
user3 = user2.copy()
user3.update({ 'name': 'fffarzan' })
print(user3)

# clearing
print(user2.clear())
print(user3)
# The set concept is unique, in all languages

my_set = {1, 2, 3, 4, 5}
my_list = [1, 2, 2, 3]

# add
my_set.add(100)
my_set.add(2) # won't add because is repetitive
print(my_set)

# converting
print(set(my_list))
print(list(my_set))

# in
print(1 in my_set)

# len
print(len(my_set))

# copy
new_set = my_set.copy()
print(new_set)

# clear
new_set.clear()
print(new_set)



first_set = {1, 2, 3, 4, 5}
second_set = {4, 5, 6, 7, 8, 9, 10}

first_set.discard(5)
print(first_set)

print(first_set.difference(second_set))
print(first_set.isdisjoint(second_set))
print(first_set.issubset(second_set))
print(first_set.issuperset(second_set))
print(first_set.intersection(second_set)) # or: print(first_set & second_set)
print(first_set.union(second_set)) # or: print(first_set | second_set)

first_set.difference_update(second_set) # remove differnce
print(first_set)
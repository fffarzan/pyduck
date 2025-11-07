# Tuples are immutable

my_tuple = (1, 2, 3, 4, 5)

# indices and ranges
print(my_tuple[1])
print(my_tuple[1:3])

# count
print(my_tuple.count(5))

# index
print(my_tuple.index(5))

# len
print(len(my_tuple))

# unpacking
x, y, *other = (6, 7, 8, 9)
print(x, y)


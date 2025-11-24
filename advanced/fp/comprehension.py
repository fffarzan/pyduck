my_list = []

for char in 'hello':
    my_list.append(char)

print(my_list) 

# list comprehension: this is exactly equal to above:
my_other_list = [char for char in 'hello']
print(my_other_list)

num_list = [num for num in range(0, 100)]
print(num_list)

num2_list = [num * 2 for num in range(0, 100)]
print(num2_list)

num2_odd_list = [num ** 2 for num in range(0, 100) if num % 2 == 0]
print(num2_odd_list)

# set comprehension
my_set = {num ** 2 for num in range(0, 100) if num % 2 == 0}
print(my_set)

# dictionary comprehension
a_dict = {
    'a': 1,
    'b': 2
}
my_dict = {k: v ** 2 for k, v in a_dict.items() if v %2 == 0}
print(my_dict)

my_other_dict = {num: num * 2 for num in [1, 2, 3]}
print(my_other_dict)

# EX1
some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

duplicates = []
for val in some_list:
    if some_list.count(val) > 1:
        if val not in duplicates:
            duplicates.append(val)

print(duplicates)

# EX1 with comprehension
duplicates2 = list(set([char for char in some_list if some_list.count(char) > 1]))

print(duplicates2)
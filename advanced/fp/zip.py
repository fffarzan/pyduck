the_list = [1, 2, 3]
other_list = [10, 20, 30]
another_list = (100, 200, 300)

print(list(zip(the_list, other_list)))
print(list(zip(another_list, other_list)))
print(list(zip(the_list, other_list, another_list)))

the_list = [1, 2, 3]

def multiply_by2(item):
    return item * 2

print(list(map(multiply_by2, the_list)))
print(the_list)

# with lambda function
print(list(map(lambda item: item * 2, the_list)))

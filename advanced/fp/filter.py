the_list = [1, 2, 3]

def check_only_odd(item):
    return item % 2 != 0

print(list(filter(check_only_odd, the_list)))
print(the_list)

# with lambda ftunction
print(list(filter(lambda item: item % 2 != 0, the_list)))

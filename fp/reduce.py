from functools import reduce

the_list = [1, 2, 3]

def accumulator(acc, curr):
    return acc + curr

print(reduce(accumulator, the_list, 10))

# with lambda function
print(reduce(lambda acc, curr: acc + curr, the_list, 10))
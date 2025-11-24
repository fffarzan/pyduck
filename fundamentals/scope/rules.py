# generally scope will be defined to clean up the memory after finishing a part of program.

# rules: order
# 1 - local
# 2 - parent
# 3 - global
# 4 - built-in python functions (like sum)

if True:
    x = 10

print(x)

def func():
    total = 100

# print(total)

a = 1

def confusion():
    a = 5
    return a

print(a)
print(confusion())
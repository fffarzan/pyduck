# sort of precedence:
# ()
# **
# * /
# + -
print(20 - 3 * 4)
print((20 - 3) + 2 ** 2)

print(2 ** 3) # power
print(5 // 4) # double divide (result rouded down to int)
print(5 % 4) # reminder

print(bin(5)) # binary version
print(int('0b101', 2)) # decimal version

# augmented assignment operator
some_value = 5
some_value += 2
print(some_value)

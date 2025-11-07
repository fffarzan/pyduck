print(True == 1) # print(True == bool(1)) => True
print('' == 1) # print(bool('') == bool(1)) => False
print([] == 1) # print(bool([]) == bool(1)) ==> False
print(10 == 10.0) # ??? ==> True (I think python can cast from float to int or vice versa)
print([] == []) # print(bool([]) == bool([])) ==> True

print('1' == 1) # checking types ==> False (I think python can't cast from string to number or vice versa)

# 'is' checks the location of memory that value is stored
print(True is 1)
print('' is 1)
print([] is 1)
print(10 is 10.0)
print([] is []) # everyime we create a list, we allocate a new memory space
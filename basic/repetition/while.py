i = 0
while i < 5:
    print(i)
    i += 1
else:
    print('more than i')

i = 0
while i < len([1, 2, 3]):
    print(i)
    break

i = 0
while i < len([1, 2, 3]):
    print(i)
    i += 1
    continue

i = 0
while i < len([1, 2, 3]):
    print(i)
    i += 1
    pass # does nothing . just continuing the loop without doing sth! a placeholder
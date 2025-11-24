for i, c in enumerate('helllloooo'):
    print(i, c)

for i, c in enumerate([1, 2, 3]):
    print(i, c)

for i, c in enumerate((1, 2, 3)):
    print(i, c)

# tricky
for i, c in enumerate(list(range(100))):
    if c == 50:
        print(f'index of 50 is: {i}')
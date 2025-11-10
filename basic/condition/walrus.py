f = 'fffarzan'

if (n := len(f)) > 7:
    print(f"hail to {n} chars!")

while (n := len(f)) > 1:
    print(n)
    f = f[:-1]

print(f)
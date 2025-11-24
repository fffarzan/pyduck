def fib_gen(i_num):
    a = 0
    b = 1

    for i in range(i_num):
        yield a
        tmp = a
        a = b
        b = tmp + b

for num in fib_gen(20):
    print(num)

def fib_list(i_num):
    a = 0
    b = 1
    res = []

    for i in range(i_num):
        res.append(a)
        tmp = a
        a = b
        b = tmp + b

    return res

print(fib_list(100))

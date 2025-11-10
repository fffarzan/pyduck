def sum(num1, num2):
    return num1 + num2

total = sum(10, 5)
print(sum(10, total))

def sum2(num1, num2):
    def another_func(n1, n2):
        return n1 + n2
    return another_func

total2 = sum2(10, 5)
print(total2(10, 10))
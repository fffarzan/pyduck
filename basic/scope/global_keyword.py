total = 0

def count():
    global total 
    total += 1
    return total

count()
count()
print(count())

def count2(total):
    total += 1
    return total

print(count2(count2(count2(total))))
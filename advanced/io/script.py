file = open('/Users/farzan/projs/python/hello/io/file.txt')

print(file)
print(file.read()) # you can read a file just once.
print(file.read())
file.seek(0) # get the cursor to whenever we want. with this trick, we can read the file again
print(file.read())
file.seek(0)

print(file.readline())
print(file.readline())
print(file.readline())
file.seek(0)

print(file.readlines())


file.close()
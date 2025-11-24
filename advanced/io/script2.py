# modes: r for read, r+ for read and write, a for append.
# absolute path and relative path
# pathlib 

with open('/Users/farzan/projs/python/hello/advanced/io/file.txt', mode='r') as file:
    print(file.readlines())

with open('/Users/farzan/projs/python/hello/advanced/io/file2.txt', mode='a') as file2:
    text2 = file2.write('hey it is me!eeee')
    print(text2)

with open('sad.txt', mode='w') as file3:
    text = file3.write(':(')

try:
    with open('sad2.txt', mode='r') as file4:
        print(file4.read())
except IOError as err:
    print('IO error')
    raise err
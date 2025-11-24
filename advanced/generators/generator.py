# range function is a generator
# iterable: is any object in python which we are able to loop through. It has __iter__ dunder.
# everything that is generator, is iterable. generator is a subset of iterators.
# with generators, we don't need hold data in memeory and make the process shorter

def gen_fn(num):
    for i in range(num):
        yield i * 2 # pauses the function

g = gen_fn(10)
print(next(g)) # resume the function
print(next(g))



def spec_forloop(iterable):
    iterator = iter(iterable)

    while True:
        try:
            print(iterator)
            print(next(iterator) * 2)
        except StopIteration:
            break

spec_forloop([1, 2, 3])

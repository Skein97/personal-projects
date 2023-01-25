
def generator_fn(num):
    for i in range(num):
        yield i*2

g = generator_fn(100)
next(g)
next(g)
print(next(g))

# for item in generator_fn(1000):
#     print(item)


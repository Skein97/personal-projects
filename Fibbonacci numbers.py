def fib(num):
    a = 1
    b = 1
    for i in range(num):
        yield a
        temp = a
        a = b
        b = temp + b


for x in fib(20):
    print(x)


def fib2(num):
    a = 1
    b = 1
    result = []
    for i in range(num):
        result.append(a)
        temp = a
        a = b
        b = temp + b
    return result

print(fib2(20))





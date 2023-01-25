# Decorator pattern
def my_decorator(func):
    def wrap_func(*args, **kwargs):
        print('**********')
        func(*args, **kwargs)
        print('**********')

    return wrap_func


# using decorator to call the func

@my_decorator
def hello(greeting, emoji = ':('):
    print(greeting, emoji)


hello('hi')

# @my_decorator
# def bye():
#     print('see ya later')


# bye()

# calling func without decorator

# def hello():
#     print('helloooo')
#
# my_decorator(hello)()

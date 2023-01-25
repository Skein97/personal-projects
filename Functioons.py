# map, filter, zip, and reduce

from functools import reduce

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

your_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]


def multiply_by2(item):
    return item * 2


def only_odd(item):
    return item % 2 != 0


def accumulator(acc, item):
       return acc + item


print(list(map(multiply_by2, my_list)))

print(list(filter(only_odd, my_list)))

print(list(zip(my_list, your_list)))

print(reduce(accumulator, my_list, 0))

print(list(map(lambda item: item*2, my_list)))

print(list(filter(lambda item: item % 2 != 0, my_list)))

print(reduce(lambda acc, item: acc + item, my_list, 0))

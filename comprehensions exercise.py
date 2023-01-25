some_list = ['a', 'b', 'c', 'd', 'b', 'm', 'n', 'n']

duplicates = list(set([item for item in some_list if some_list.count(item) > 1]))

print(duplicates)
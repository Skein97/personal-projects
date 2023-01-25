from collections import Counter, defaultdict, OrderedDict

# li = [1, 2, 3, 3, 4, 5, 6, 7, 8]
# sentence = 'blah blah blah thinking about python'
#
# print(Counter(li))
# print(Counter(sentence))
# # Counter creates a dictionary of the number of times an item occurs in the iterable

# dic = defaultdict(lambda: 'not present', {'a': 1, 'b': 2})
# print(dic['c'])
# # replaces an error message with a default value

d = OrderedDict()
d['a'] = 1
d['b'] = 2

d2 = OrderedDict()
d2['b'] = 2
d2['a'] = 1

print(d2 == d)

d = {'c': 3}
d['a'] = 1
d['b'] = 2

d2 = {'c': 3}
d2['b'] = 2
d2['a'] = 1

print(d2 == d)

# Retains the order of input of dictionary (obsolete from py v 3.8)


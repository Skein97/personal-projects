# dict with value is key * 2
# my_dict2 = {num: num*2 for num in [1, 2, 3]}
# print(my_dict2)
#
#
# my_dict3 = [str(num * 100).zfill(4) for num in range(0, 24, 1)]
# print(my_dict3)



time = [str(num * 100).zfill(4) for num in range(0, 2, 1)]
wsi = [input('wsi value: ') for i in range(2)]
daily_wsi = dict(zip(time, wsi))




print(daily_wsi2)


# def time():
#     for i in range(0, 24, 1):
#         j = i * 100
#         return str(j).zfill(4)
#
# print(time())



# list, set, dictionary
#
# # list
# # generate list of characters word
# my_list = [char for char in 'hello']
#
# # generate list of numbers in range
# my_list2 = [num for num in range(100)]
#
# # generate list of squares
# my_list3 = [num ** 2 for num in range(100)]
#
# # generate list of even squares
# my_list4 = [num ** 2 for num in range(100) if num % 2 == 0]
#
# print(my_list)
# print(my_list2)
# print(my_list3)
# print(my_list4)
#
# # set
# # generate set of characters word
# my_set = {char for char in 'hello'}
#
# # generate  of numbers in range
# my_set2 = {num for num in range(100)}
#
# # generate set of squares
# my_set3 = {num ** 2 for num in range(100)}
#
# # generate set of even squares
# my_set4 = {num ** 2 for num in range(100) if num % 2 == 0}
#
# print(my_set)
# print(my_set2)
# print(my_set3)
# print(my_set4)
#
# # dictionary
# simple_dict = {
#     'a': 1,
#     'b': 2
# }
# my_dict = {k: v ** 2 for k, v in simple_dict.items() if v % 2 ==0}
#
# print(my_dict)

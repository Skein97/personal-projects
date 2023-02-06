import sys
from translate import Translator

try:
	with open('test.txt', mode='r') as my_file:
		translator = Translator(to_lang= sys.argv[1])
		text = my_file.read()
		print(text)
		translation = translator.translate(text)
		print(f'translated to {translation}')
		with open('test2.txt', mode='a') as my_file2:
			my_file2.write(f'\n{translation}')	
except FileNotFoundError as e:
	print('check your file path silly')




#from_lang = sys.argv[1]




# with open('sad.txt', mode='w') as my_file:
# 	text = my_file.write(':(')
# 	print(text)
# 	#print(my_file.readlines())






# # Input output basics

# # my_file = open('test.txt')

# # print(my_file.readlines())


# # # my_file.seek(0)
# # # print(my_file.read())
# # # my_file.seek(0)
# # # print(my_file.read())

# # my_file.close()

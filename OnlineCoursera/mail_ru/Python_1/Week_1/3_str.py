# example_string = "Python's course"
# print(example_string)
#
# example_string = 'Python\'s course'
# print(example_string)
#
# example_string = r"Python's course"
# print(example_string)
#
# example_string = "Python's" \
#                     " course"
#
# print(example_string)
#=======================================================================
"""Slice
[start:stop:step]
"""

# example_string = "Python's Course on Coursera"
#
# print(example_string[9:])   # >>> Course on Coursera
# print(example_string[9:15]) # >>> Course
# print(example_string[-8:]) # >>> Coursera


# example_string = '0123456789'
# print(example_string[::2])
#
# example_string = 'Moscow'
# print(example_string[::-1])

# quote = """Болтовня ниего не стоит. Покажи мне код."""
# print(quote.count('о'))  # >>> 6
#
# print('moscow'.capitalize()) # >>> Moscow
# print('2017'.isdigit())  # >>> True
#
# print(dir(str))

#====================================================================

# print('3.14' in 'Pi = 3.1415926')

#====================================================================

# example = 'Moscow is the great capital of Russia'
# for letter in example:
#     print('Letter', letter)
#====================================================================
# num_str = str(999.01)
# print(type(num_str))
#
# print(bool('Empty string'))
#====================================================================

# example = '%d это число, которое мы берем и умножаем на %d'
# print(example%(5,6)) #>>>5 это число, которое мы берем и умножаем на 6
#
#
# example = '%s is a capital of %s'
# print(example%('Moscow', 'Russia')) #>>>Moscow is a capital of Russia
#====================================================================

# print("{} не лгут, но {} пользуются формулами. ({})".format("Цифры", "лжецы"
#                                                       , "Robert A.Heinlein"))
#
#
# print("{num} Кб должно хватить для любых задач. ({author})".format(
#     num = 640, author="Bill Gates"
# ))
#
# subject = "optimisation"
# author = "Donald Knuth"
#
# print(f'Early {subject} - the mean of all evils. ({author})')
#====================================================================
"""Модификаторы форматирования"""

# num = 8
# print(f"Binary: {num:#b}")
#
# num = 2 / 3
# print(num)
# print(f"{num:.3f}")
#====================================================================
# name = input("Введите ваше имя: ")
#
# print(f"Привет, {name}!")
#====================================================================
"""Байтовые строки"""
# examlpe_bytes = b"hello"
# print(type(examlpe_bytes)) #>>> <class 'bytes'>
#
# for element in examlpe_bytes:
#     print(element)

example_string = "привет"
encoded_string = example_string.encode(encoding = "utf-8")
print(encoded_string) #>>> b'\xd0\xbf\xd1\x80\xd0\xb8\xd0\xb2\xd0\xb5\xd1\x82'
print(type(encoded_string)) #>>> <class 'bytes'>


decoded_string = encoded_string.decode()
print(decoded_string) #>>> привет










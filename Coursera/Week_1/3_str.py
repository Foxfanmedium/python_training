# example_string = "Course about \"Python\" on \"Coursera\""
# print(example_string)

#======================================================================================================================
# example_string = "Some files on c:\\\\"
# print(example_string)
#
# example_string = r"Some files on c:\\"
# print(example_string)

#======================================================================================================================
# example_string = "Perl - это язык, который одинаково " \
#                 "выглядит как до, так и после RSA шифрования." \
#                     "(Keith Bostic)"
# print(example_string)
#======================================================================================================================

# example_string = """
# Есть всего два типа языков программирования: те, на которые
# люди все время ругаются, и те, которые никто не использует.
# Bjarne Stroustrup
# """
# print(example_string)
#======================================================================================================================
# a = "All good" + " in our life!"
# print(a)
# print(a *3)
#======================================================================================================================
# example_string = "Hello"
# print(id(example_string))
# example_string += ", world!"
# print(id(example_string))
#======================================================================================================================
# example_string = "Course of Python on Coursera"
# print(example_string[9:])
#
# example_string = "0123456789"
# print(example_string[::2])
# example_string = "Moscow"
# print((example_string[::-1]))
#======================================================================================================================
# quote = """Talking is nothing! Show me the code!
# Linus Torvalds"""
# print(quote.count("o"))
# print(quote)
#
# capital = "moscow"
# print(capital.capitalize())
#
# number = "2017"
# print(number.isdigit())
#======================================================================================================================
# example_string = "Hello"
#
# for letter in example_string:
#     print("Letter", letter)
#======================================================================================================================
# template = "%s - главное достоинство программиста. (%s)"
# print(template % ("Лень", "Larry Wall"))
#
# template = "{} не лгут, но {} пользуются формулами. ({})"
# print(template.format("Цифры", "лжецы", "Robert A. Heinlein"))
#
# template = "{num} не лгут, но {name} пользуются формулами. ({author})"
# print(template.format(num="Цифры", name="лжецы", author="Robert A. Heinlein"))
#
# subject = 'optimization'
# author = "Donald Knuth"
# print(f"Преждевременная {subject} - корень всех зол. ({author}) ")
#======================================================================================================================
# num = 8
# print(f"Binary: {num:#b}")
#
# num = 2 / 3
# print(num)
#
# print(f"{num:.3f}")
#======================================================================================================================
# name = input("Insert your name: ")
# print("Hello, %s" %(name))
# print(f"Hello, {name}")
#======================================================================================================================
# example_string = b"Hello"
# print(type(example_string)) # >>> <class 'bytes'>
#
# for element in example_string:
#     print((element))

example_string = "привет"
print(type(example_string))
print(example_string)

encoded_string = example_string.encode(encoding="utf-8")
print(type(encoded_string)) # >>>  <class 'bytes'>
print(encoded_string) # >>>   b'\xd0\xbf\xd1\x80\xd0\xb8\xd0\xb2\xd0\xb5\xd1\x82'

decoded_string = encoded_string.decode()
print(decoded_string)








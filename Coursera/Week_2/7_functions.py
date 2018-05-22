# from datetime import datetime
#
# def get_seconds():
#     """Return current seconds"""
#     return datetime.now().second
#
# print(get_seconds())
#
# get_seconds.__doc__ # получение документационную строку
# get_seconds.__name__  # Получение имени функции
#=====================================================================================================================
# def split_tags(tag_string):
#     tag_list = []
#     for tag in tag_string.split(','):
#         tag_list.append(tag.strip())
#     return tag_list
#
# print(split_tags('python, coursera, mooc'))
#=====================================================================================================================
# http://bdseo.ru/kak-chitat-dannye-s-pdf-cherez-python-3-pypdf2
# import PyPDF2
#
#
# def read_book():
#     pl = open('testing.pdf', 'rb')
#     plread = PyPDF2.PdfFileReader(pl)
#     getpage37 = plread.getPage(37)
#     read_all = getpage37.extractText()
#     list_word = []
#     for word in read_all.split(','):
#         list_word.append(word.strip())
#     return list_word
#
# print(read_book())
#=====================================================================================================================
# def add(x: int, y: int) -> int:
#     return x + y
#
#
# print(add(5, 20))
#=====================================================================================================================


# def extender(source_list, extend_list):
#     source_list.extend(extend_list)
#
# values = [1, 2, 3, 4, 5, 6]
# extender(values, [7, 8, 9, 10])
#
# print(values)
#=====================================================================================================================

# def say(greeting, name):
#     print('{} {}!'.format(greeting, name))
#
#
# say('Hello', 'Kitty')
# say(name='Kitty', greeting='Hello')
#=====================================================================================================================
def printer(*args):
    print(type(args))

    for argument in args:
        print(argument)

printer(1,2,3,4,5,6,7)







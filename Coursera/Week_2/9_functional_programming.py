# def caller(func, params):
#     return func(*params)
#
# def printer(name, origin):
#     print('I\'m {} of {}!'. format(name, origin))
#
# caller(printer, ['Moana', 'Motunui'])
#=====================================================================================================================
# def get_multiplier():
#     def inner(a, b):
#         return a * b
#     return inner
#
#
# multiplier = get_multiplier()
# print(multiplier(10, 11))
# #=====================================================================================================================
# def get_multiplier(number):
#     def inner(a):
#         return a * number
#     return inner
#
# multiplier_by_2 = get_multiplier(2)
# print(multiplier_by_2(10))
#=====================================================================================================================
# def squarify(a):
#     return a ** 2
# """
# Функциональный подход в данном случае.
# Функция map принмиает в себя другую функцию и итерабельный объект, для возврата списка используем ф-ию list
# """
# f = list(map(squarify, range(5)))
# print(f)
#=====================================================================================================================
# """
# Другая полезная функция это filter.
# Она позволяет фильтровать значения функции по какому-то предикату.
# """
#
# def is_positive(a):
#     return a > 0
#
# f = list(filter(is_positive, range(-5, 7)))
# print(f)
#=====================================================================================================================
# print(list(map(lambda x: x**2, range(5))))
#
# print(list(filter(lambda x: x > 2, range(-9, 20))))
#=====================================================================================================================
# def stringify_list(num_list):
#     return list(map(str, num_list))
#
# print(stringify_list(range(10)))
#=====================================================================================================================
# from functools import reduce
#
# def multiply(a,b):
#     return a * b
#
# print(reduce(multiply, [1,2,3,4,5])) #>>> 120 - попеременное умножение цифр в списке с целью сжать до одного
#=====================================================================================================================
# from functools import reduce
#
# print(reduce(lambda x, y: x * y, range(1, 5))) # >>> 24
# print(reduce(lambda x, y: x * y, range(-5,-2))) # >>> -60
#=====================================================================================================================
# from functools import partial
#
# def greeter(person, greeting):
#     return '{}, {}!'.format(greeting, person)
#
# hier = partial(greeter, greeting = 'Hi')
# helloer = partial(greeter, greeting = 'Hello')
#
# print(greeter('dear', 'Good morning'))
# print(hier('brother'))
# print(helloer('sir'))
#=====================================================================================================================
# Создать список квадратов чисел из оригинального списка
# использование цикла for
# origin_list = [0,1,2,3,4,5,6,7,8,9]
# squar_list = []
# for num in origin_list:
#     squar_list.append(num ** 2)
# print(squar_list)
#
# # использование анонимных функций
# squar_list_2 = list(map(lambda x: x **2, origin_list))
# print(squar_list_2)
#
# # list comprehensive - списочные выражения работает быстрее чем циклы for
# squar_list_3 = [number ** 2 for number in origin_list]
# print(squar_list_3)
#
# squar_list_4 = [x ** 2 for x in range(20)]
# print(squar_list_4)

# squar_list_5 = [num ** 2 for num in range(-5, 10)]
# print(squar_list_5)
#=====================================================================================================================
# even_list = []
# origin_list = [2, 0, 4, 16, 22, 25, 89, 64, 52, 25]

# for num in origin_list:
#     if num % 2 == 0:
#         even_list.append(num)
# print(even_list)
#
#
# even_list_2 = [num for num in range(-8, 20) if num % 2 == 0]
# print(even_list_2)
#
# square_map = {number: number **2 for number in range(-5, 10)}
# print(square_map)

# reminder_set = {number % 10  for number in range(100)}
# print(reminder_set)


first_list = range(7)
second_list = [x ** 2 for x in first_list]
print(first_list) # >>> range(0, 7)
print(second_list) # >>> [0, 1, 4, 9, 16, 25, 36]
print(list(zip(first_list, second_list))) # >>> [(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25), (6, 36)]















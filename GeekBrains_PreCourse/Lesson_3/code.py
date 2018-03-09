# print('asda')
# # input()
# len('asdasd')
# int()
# bool()
# float()
# str()

# x = '1 2 3'
# print(x.split(' ', 1))
# print(x.rsplit(' ', 1))

# for i in range(1, 11):
#     print(i)

# print(abs(-100))

# print(max([1, 2, 3, 4, 5]))

# a = ['qwe', 'asd', 'zxc']
#
# for index, elem in enumerate(a, start=1):
#     print(index, elem)

# a = {100, 200}
#
# for index, value in enumerate(a):
#     print(index, value)

# def check_name(name_for_check):
#     print(name_for_check.title())
#
# name = 'ивАн пЕтров иВанович'
# check_name(name)

# def check_name(name_for_check):
#     return name_for_check.title()
#
# name = 'ивАн пЕтров иВанович'
# result = check_name(name)
# print(result)

# y = 100
#
# def check_name(surname, name, middle_name):
#     x = 20
#
#     # global y
#     y = 10
#     print(surname, name, middle_name)
#
# print(x)
#
# check_name('Petrov', 'Ivan', 'Ivanovich')


# def check_name(surname, name, middle_name=''):
#     print(surname, name, middle_name)
#
# check_name('Иванов', 'Иван')
# check_name('Иванов', 'Иван', 'Иванович')

# def check_name(*args):
#     print(args)
#     for arg in args:
#         print(arg.title())
#
# check_name('ivan petrov', 'oleg ivanov')
#
# names = ['ivan petrov', 'oleg ivanov']
# check_name(*names)
#
# check_name()

# def check_name(name, surname='', *args):
#     print(name, surname, args)

# def check_name(name, surname='', middle_name=''):
#     print(name, surname, middle_name)
#
# check_name('Иван', middle_name='Петрович')

# def check_name(*args, **kwargs):
#     print(args, kwargs)
#
# check_name(1,2,3, name='Ivan', age=20)

# def check_name(**kwargs):
#     print(kwargs)
#
# person = {'name': 'Ivan', 'age': 20}
# # check_name(name='Ivan', age=20)
# check_name(**person)

# names = ['Ivan', 'Alice', 'Ivan']
# salary = [300, 400, 500]
# print(dict(zip(names, salary)))

# def test(x):
#     return x ** 2
#
# def filter_test(x):
#     return x > 0
#
#

# print(list(map(lambda x: x ** 2, [1, 2, 3, 4, 5, 6])))
# print(list(filter(lambda x: x > 0, [-1, -2, -3, 4, 5, 6])))

# file = open('100.txt')
# # print(file.readlines())
# for line in file:
#     print(line.strip())
# file.close()

# file = open('100.txt', 'a+', encoding='UTF-8')
# file.write('100\n')
# file.close()

# with open('100.txt') as file:
#     print(file.readlines())

import os

print(os.path.join('home', 'sizov', '100.txt'))

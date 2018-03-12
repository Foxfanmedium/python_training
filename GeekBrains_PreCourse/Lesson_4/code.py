# a = 4
# b = 5
# c = 'asd'
# d = 4.4
# e = True
# f = (1, 2, 3)
#
# def test(some_data):
#     some_data = 100
#
# test(a)
# print(a)

# a = [1, 2, 3, 4]
#
# def test(some_list):
#     some_list[0] = 100
#
# test(a)
# print(a)

# some_list = [1, 2, 3, 4]
#
# for i in some_list.copy():
#     print(i)
#     some_list.remove(i)
# import copy
#
# some_list = [1, 2, 3, 4, [5, 6, 7]]
# # new_list = some_list.copy() # срез работает так же.
# new_list = copy.deepcopy(some_list)
#
# some_list[4][0] = 100
#
# print(some_list, new_list)

# a = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
#
# a[1][1]

# name = input('Name:')
# print(name or 'Гость')

# name = input('Name:')
# print(name if name else 'Гость')

# age = int(input('Age:'))
# print('Доступ разрешен' if age >= 18 else 'В доступе отказано!')

# a = 10
# b = 10
# print(a is b)
#
# a = 11
# print(a is b)

# some_list = [1, 2]
# new_list = some_list.copy()
# print(some_list is new_list)

# some_list = []
#
# for i in range(10):
#     some_list.append(i)
#
# print(some_list)
#
# some_list = [i ** 2 for i in range(10)]
# print(some_list)
#
# my_range = (-1, 1, 2, 3)
#
# some_list = []
# for i in my_range:
#     if i > 0:
#         some_list.append(i)
#
# some_list = [i for i in my_range if i > 0]
# print(some_list)

# def gen_list():
#     temp_list = []
#     for i in range(10):
#         temp_list.append(i)
#     return temp_list
#
# my_list = gen_list()


# data = (('Alex', 100), ('Alice', 200), ('Bob', 300))
# my_dict = {key: value for key, value in data}
# print(my_dict)

# my_str = r'Hello\tworld\n'
# print(my_str)

# import re
#
# email = 'test123@mail.com'
# regex = '[a-zA-Z0-9]+@[a-zA-Z]+\.com'
# # print(re.match(regex, email)) # Ищет строго с начала строки
# print(re.search(regex, email))
# print(re.findall(regex, email))
#
# if email in re.findall(regex, email):
#     print('Ваш email в списке валидных!')
# else:
#     print('Ваш email не корректный.')

some_list = [1, 2, 3]

try:
    age = int(input('Age:'))
    some_list[0]
    100 / 0
except ValueError:
    print('Вы должны ввести число!')
except IndexError:
    print('Укажите корректный индекс!')
except ZeroDivisionError:
    print('На ноль делить нельзя!')
except Exception as e:
    print(e, e.__class__)
else:
    print('Исключений не было!')
finally:
    print('Выполнится в любом случае!')

print('...')

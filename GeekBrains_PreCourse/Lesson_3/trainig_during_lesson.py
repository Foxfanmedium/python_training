# for i in range(10):
#     print(i)

# for i in range(1, 11):
#     print(i)
#=============================================================================
# print(abs(-100))
#=============================================================================
# list_max = [50, 100, 8, -6, 8, 0, 100500]
# print(max(list_max))
# print(min(list_max))
#=============================================================================
# list_symbols = ['abc', 'qwerty', 'qaxc', '-5djhgvkjsabfvhsabvjsk', 'sdvghuaskvbasbvahsd', '451646846846384684461186466']
# print(max(list_symbols))
# for index, element in enumerate(list_symbols, start=1):
#     print("'", index,  "'","-",  element)
#=============================================================================
# a = {1: 100, 2: 200, 3: 300, 4: 400}
# for key, value in a.items():
#     print(key, value)
#=============================================================================
#
# def check_name(name_for_check):
#     return name_for_check.title()
#
# name = 'ивАн пЕтров иВанович'
# result = check_name(name)
# print(result)
#=============================================================================
# x = '1 2 3'
# print(x.split(' ', 1))
# print(x.rsplit(' ', 1))
#
# a = '10 15 25 100'
# print(a.split(' '))
#=============================================================================
# def check_name(surname, name, middle_name = ''):
#     print(surname, name, middle_name)
#
# check_name('Иванов', 'Иван')
# check_name('Иванов', 'Иван', 'Иванович')
#=============================================================================
# def check_name(*args):
#     print(args)
#     for arg in args:
#         print(arg.title())
#
# check_name('ivan', 'ivanov')
# check_name('ivan ivanov', 'petrov petr')
#=============================================================================
# def check_name(*args):
#     print(args)
#     for arg in args:
#         print(arg.title())
#
# names = ['ivan ivanov', 'petrov petr']
# check_name(*names)
#=============================================================================
# def check_name(name, surname= '', *args):
#     print(name, surname, args)
#============================================================================


# def check_name(name, surname='', middle_name=''):
#     print(name, surname, middle_name)
#
#
# check_name('ivan', middle_name='petrovich')
#============================================================================
# def check_name(**kwargs):   # формирует словарь
#     print(kwargs)
#
# check_name(name = 'Ivan', age = 20, surname = 'Petrov')

# def check_name(*args, **kwargs):
#     print(args, kwargs)
#
# check_name(1, 2, 3, name='Ivan', age=20, surname='Petrov')
#============================================================================
# def check_name(**kwargs):
#     print(kwargs)
#
# person = {'name':'Ivan', 'age':20}
# check_name(**person)
#============================================================================
# names = ['Ivan', 'Alice']
# salary = [300, 400]
# print(zip(names, salary))
# print(dict(zip(names, salary)))
# print(tuple(zip(names, salary)))
# print(list(zip(names, salary)))
# print(set(zip(names, salary)))
#============================================================================
def test(x):
    return x**2

def filter_test(x):
    return x > 5

print(map(test, [1,2,3,4,5,6,7,8,9,10]))
print(list(map(test, [1,2,3,4,5,6,7,8,9,10])))
# print(list(filter(filter_test, [1,2,3,4,5,6,7,8,9,10])))
#============================================================================

# print(map(lambda x: x ** 2, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
# print(list(map(lambda x: x ** 2, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])))
# print(list(filter(lambda x: x > 0, [-1, -2, -3, 4, 5, 6, 7, 8, 9, 10])))
# print(list(map(lambda x, y = 5: x ** 5, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])))
#============================================================================
# file = open('100.txt')
# print(file.readlines())  # если будет введено print(file.readline()) то прочитает только первую строку
# file.close()
#============================================================================
# file = open('100.txt')
# for line in file:
#     print(line)
# file.close()
#============================================================================
# file = open('100.txt')
# for line in file:
#     print(line.strip())  # strip срезает все знаки табуляции, переноса строки и т.д.
# file.close()
#============================================================================
# file = open('100.txt', 'r')    # 'w'- write,   'a' - append   'rb' - Работа с бинарными фалыми(картинки, и т.д)
                                 # 'a+'- чтение и добавление,   'w+' - чтение и дозапись
# file = open('100.txt', 'a', encoding='UTF-8')
# file.write('100\n')
# file.close()
#============================================================================
# with open('100.txt') as file:
#     print(file.readlines())
#     print(file.readlines())
# ============================================================================
# import os
# print(os.path.join('home', 'zakirov', '100.txt'))
# ============================================================================
# with open('100.txt') as file:
#     for line in file:
#         # line = line.strip()
#         # print(line)
#         print(line.strip())
# ============================================================================


# s = set() # создание пустого множества
# s.add(element)
# s.revome(element)  # есди эдемента нет, то появиться ошибка
# s.discard(element)    # ксли элемента нет, то ошибок не будет
# s.clear(element)
# len(s)  # узнать число элементов в множестве

# basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
# for x in basket:
#     print(x)    # выводи на экран будет неупорядоченного множества
#-----------------------------------------------------------------------------------------------------------------------
#Dictionary
# dict{}  # создание пустого словаря
# d = {'a':239, 10:100500}
# print(d['a'])
# print(d[10])
#-----------------------------------------------------------------------------------------------------------------------
# dictionary= {...}
# key in dictionary  # True or False
# key not in dictionary   # True or False
# dictionary[key] = value
# dictionary [key]
# dictionary.get(key)
# del dectionary[key]


# Перебор элементов словаря
# d = {'C':14, 'A':12, 'T':9, 'G':18}
# for key in d :
#     print(key, end=" ")
# for key in d.keys():
#     print(key, end=" ")
# for value in d.values():
#     print(value, end=" ")
# for key, value in d.items():
#     print(key, value, end=" ")

# Напишите функцию update_dictionary(d, key, value), которая принимает на вход словарь d и два числа: key и value.
# Если ключ key есть в словаре d, то добавьте значение value в список, который хранится по этому ключу.
# Если ключа key нет в словаре, то нужно добавить значение в список по ключу 2⋅key. Если и ключа 2⋅key нет,
# то нужно добавить ключ 2⋅key в словарь и сопоставить ему список из переданного элемента [value].
# Требуется реализовать только эту функцию, кода вне неё не должно быть.
# Функция не должна вызывать внутри себя функции input и print.

# def update_dictionary(d, key, value):
#     if key in d:
#         d[key].append(value)
#     elif 2*key in d:
#         d[2*key].append(value)
#     else:
#         d[2*key] = []
#         d[2*key].append(value)

#-----------------------------------------------------------------------------------------------------------------------
# Когда Антон прочитал «Войну и мир», ему стало интересно, сколько слов и в каком количестве используется в этой книге.
# Помогите Антону написать упрощённую версию такой программы, которая сможет подсчитать слова, разделённые пробелом и
# вывести получившуюся статистику.
# Программа должна считывать одну строку со стандартного ввода и выводить для каждого уникального слова в этой строке
# число его повторений (без учёта регистра) в формате "слово количество" (см. пример вывода).
# Порядок вывода слов может быть произвольным, каждое уникальное слово должно выводиться только один раз

# n='' #инициализация строки
# n = str(input())
# m = [] #инициализация списка
# m.append([str(s.lower()) for s in n.split()])
# d = {} #инициализация пустого словаря
# li, lj = len(m), len(m[0])
# for i in range(li):
#     for j in range(lj):
#         p = m[i][j]
#         if p in d:
#             d[p]+=1
#         else:
#             d[p] = 1
# for key,value in d.items():
#    print(key,value)

#-----------------------------------------------------------------------------------------------------------------------
# Имеется реализованная функция f(x), принимающая на вход целое число x, которая вычисляет некоторое
# целочисленое значение и возвращает его в качестве результата работы.
# Функция вычисляется достаточно долго, ничего не выводит на экран, не пишет в файлы и зависит только
# от переданного аргумента x.
# Напишите программу, которой на вход в первой строке подаётся число n — количество значений x,
# для которых требуется узнать значение функции f(x), после чего сами эти n значений, каждое на
# отдельной строке. Программа должна после каждого введённого значения аргумента вывести соответствующие
# значения функции f на отдельной строке.
# Для ускорения вычисления необходимо сохранять уже вычисленные значения функции при известных аргументах.
# Обратите внимание, что в этой задаче установлено достаточно сильное ограничение в две секунды по
# времени исполнения кода на тесте.

# d={}
# k=[]
# n=int(input())
# for i in range(n):
#     x = int(input())
#     k.append(x)
# for j in range(0,len(k)):
#     key=k[j]
#     if  key in d:
#         print(d[key])
#     elif key not in d:
#         p = k[j]
#         d[key]=f(p)
#         print(d.get(key))
#-----------------------------------------------------------------------------------------------------------------------
# Чтение из файла

# inf = open('file.txt', 'r')
# s1 = inf.readline()
# s2 = inf.readline()
# inf.close()    # открытие файла, чтение 2-х строк и закрытие файла

# with open('file.txt') as inf:
#     s1 = inf.readline()
#     s2 = inf.readline()   # в этой конструкции файл сам закрывается

# s = inf.readline().strip()
# '\t abc \n'.strip() -> 'abc'
# os.path.join('.', 'dirname', 'filename.txt') -> './dirname/filename.txt'

#Построчное чтение файла
# with open 'input.txt' as inf:
#     for line in inf:
#         line = line.strip()
#         print(line)

#Запись в файл

# ouf = open('file.txt', 'w')
# ouf.write('Some text\n')
# ouf.write(str(25))
# ouf.close()
#
# with open('text.txt', 'w') as ouf:
#     ouf.write('Some text\n')
#     ouf.write(str(25))

#-----------------------------------------------------------------------------------------------------------------------
# import re
#
# # with open('dataset_3363_2.txt', 'r') as string:
# #     s1 = re.split("(\d*)", string.readline())[:-1]
# #     print(''.join([i[1] * int(i[0]) for i in zip(s1[1::2], s1[::2])])
#
#
# # s1 = 'a3b4c2e10b1'
# # s1 = re.split("(\d*)", s1())[:-1]
# # print(s1)
# # # print(''.join([i[1] * int(i[0]) for i in zip(s1[1::2], s1[::2])])
# # #-------------------------------------------------------------------------------------------------------------------
# # Под вопросом - перерешать
# # import sys
# # import string
# #
# # with open('dataset_3363.txt', 'r') as f:
# #     a = f.readlines()
# # a = [i.strip().lower() for i in sys.stdin.readlines()]
# # a = " ".join(a).split(' ')
# # d = {}
# # for i in a:
# #     d[i] = a.count(i)
# # print(d)
# # d = sorted(d.items(), key=lambda x: x[1], reverse=True)
# # print(d)
# # print(d[0][0], d[0][1])
# #-----------------------------------------------------------------------------------------------------------------------
#
# # Под вопросом - перерешать
# # count = 0
# # lst = []
# # with open('dataset_4.txt') as file:
# #     for string in file:
# #         string = string.strip().split(';')
# #         for i in string[1::]:
# #             count += int(i)
# #         print(count / 3)
# #         string.append(count / 3)
# #         # print(string)
# #         lst.append(string)
# #         count = 0
# #
# # math = 0
# # phys = 0
# # rus = 0
# # for i in lst:
# #     math += int(i[1])
# #     phys += int(i[2])
# #     rus += int(i[3])
# # print(math / len(lst), phys / len(lst), rus / len(lst))
# #-----------------------------------------------------------------------------------------------------------------------
# # Напишите программу, которая подключает модуль math и, используя значение числа π из этого модуля,
# # находит для переданного ей на стандартный ввод радиуса круга периметр этого круга и выводит его на стандартный вывод.
# # Sample Input:
# # 10.0
# # Sample Output:
# # 62.83185307179586
#
#
# # import math
# # r = float(input('Введите радиус круга:'))
# # p = math.pi*r*2
# # print(p)
# #-----------------------------------------------------------------------------------------------------------------------
# # Напишите программу, которая запускается из консоли и печатает значения всех переданных аргументов на экран
# # (имя скрипта выводить не нужно). Не изменяйте порядок аргументов при выводе.
# # Для доступа к аргументам командной строки программы подключите модуль sys и используйте переменную argv из этого модуля.
# # Пример работы программы:
# # > python3 my_solution.py arg1 arg2
# # arg1 arg2
#
# # import sys
# # s = ''
# # s2 = ''
# # for i in range(1,len(sys.argv)):
# #     s = s + sys.argv[i]+' '
# # s2 = s
# # print(s2,end=' ')
# #-----------------------------------------------------------------------------------------------------------------------
# # Скачайте файл. В нём указан адрес другого файла, который нужно скачать с использованием модуля requests и посчитать
# # число строк в нём.
# # Используйте функцию get для получения файла (имеет смысл вызвать метод strip к передаваемому параметру, чтобы убрать
# # пробельные символы по краям).
# # После получения файла вы можете проверить результат, обратившись к полю text. Если результат работы скрипта не
# # принимается, проверьте поле url на правильность. Для подсчёта количества строк разбейте текст с помощью
# # метода splitlines.
# # В поле ответа введите одно число или отправьте файл, содержащий одно число.
#
#
# import requests
# lines = 0
#
# with open('dataset_3378_2.txt') as site:
#     site = site.read().strip()
#     filo = requests.get(site)
#     for i in filo.text.splitlines():
#         lines += 1
#     print(lines)
#-----------------------------------------------------------------------------------------------------------------------


































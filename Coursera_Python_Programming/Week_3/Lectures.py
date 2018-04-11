# x = float(input())
# y = float(input())
# print(x + y)
# if 0.1 + 0.2 == 0.3:
#     print("YES")
# else:
#     print("NO")
# print('{0:.25f}'.format(0.1))
#print(0.1.as_integer_ratio())
#print(float(2**100).as_integer_ratio())
#print(11%2.5)
# ======================================================

# import math

# print(int(2.5),int(3.5), int(-2.5))
# print(math.floor(2.5), math.floor(3.5), math.floor(-2.5))
# print(math.ceil(2.5), math.ceil(3.5), math.ceil(-2.5))
# print(round(2.9), round(3.1), round(-2.55)) - округление до ближайшего четного числа
# ========================================================
# from math import floor, ceil, sqrt
# print(int(2.5),int(3.5), int(-2.5))
# print(floor(2.5), floor(3.5), floor(-2.5))
# print(ceil(2.5), ceil(3.5), ceil(-2.5))
# print(round(2.9), round(3.1), round(-2.55))
# print(sqrt(2))
# ========================================================

# s = 'abcdef'
# print(s[0])
# print(len(s)) - определение длинны строки от 0 и до...
# print(s[-2]) - предпоследняя буква
# print(s[0:2])  - срез с первого символа каждого четного числа
# print(s[1:])  - срез со второно по последний символ
# print(s[::2]) - срез символов стоящих на четных местах: с самого начала,по самый конец,с шагом 2
# print(s[1::2]) - срез символов стоящих на нечетных местах: с самого начала,по самый конец,с шагом

# s = 'abcd abc abd'
# print(s.find('abd'))
# print(s.find('abe')) - результат будет "-1", что значит что подстрока не найдена

# s = 'abcd abc abd'
# pos = 0
# while s.find('abc', pos) != -1:
#     print(s.find('abc', pos))
#     pos = s.find('abc', pos) + 1

# ========================================================
# поиск при помощи метода rfind
# s = 'abcd abc abd'
# print(s.rfind('abc'))

# s = 'abcd abc abd'
# print(s.replace('abc', '1234')) - все вхождения будут заменены

# s = 'abcd abc abd'
# print(s.replace('abc', '1234', 1)) сколько вхождений будет заменено

# s = aaaaaa
# print(s.replace('aa', 'a'))

# s = 'aaaaaa'   печать одной буквы а
# while s.find('aa') != -1:
#     s = s.replace('aa', 'a', 1)
# print(s)

# s = 'aaaaaa'   печать нескольких строк с уменьшением колличества букв а
# while s.find('aa') != -1:
#     s = s.replace('aa', 'a', 1)
#     print(s)

# s = 'abcdferacbabc'
# print(s.count('abc'))  подсчет сколько раз встречается abc

# s = 'aaaaaa'
# print(s.count('aa'))  # подсчет сколько раз встречается aa

# s = 'aaaaaa'
# print(s.count('aa', 1)) подсчет сколько раз встречается aa начиная со второго символа































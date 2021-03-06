# https://www.youtube.com/watch?v=jw3lws60HzY
# https://geekbrains.ru/events/886

"""
Словарь - неупорядочная коллекция произвольных объектов с доступом по ключу
"""

# directors = [("Райан Джонсон", "Звездные войны: Последний Джедай"),
# ("Дэвид Литч", "Дэдпул 2"), ("Гай Ричи", "Меч короля Артура")]
#
# director = "Дэвид Литч"
#
# for d, f in directors:
#     if d == director:
#         print(f)
#         break
# else:
#     print("Not Found")

# >>> Дэдпул 2
#==========================================================================

"""
Creating of dictionaries by two ways: 
"""

# d = {}
# print(d)
# d = dict()
# print(d)
# d = dict(a="first", c="second")
# print(d)

#==========================================================================

# directors = [{"Райан Джонсон", "Звездные войны: Последний Джедай"},
# {"Дэвид Литч", "Дэдпул 2"}, {"Гай Ричи", "Меч короля Артура"}]
#
# d = dict(directors)
# print(d)
#
# d = dict([(1, "first"), (2, "second"), (3, "third")])
# print(d)

#==========================================================================

# Generator of dictionaries
# d = {i: i **3 for i in range(10)}
# print(d)
# >>> {0: 0, 1: 1, 2: 8, 3: 27, 4: 64, 5: 125, 6: 216, 7: 343, 8: 512, 9: 729}

# d = {i: i **3 for i in range(10) if i%2 == 0}
# print(d)
# >>> {0: 0, 2: 8, 4: 64, 6: 216, 8: 512}

#==========================================================================

"""
Work with dictionaries 
"""

# Получение доступа к значению по ключу

# directors = [{"Райан Джонсон", "Звездные войны: Последний Джедай"},
# {"Дэвид Литч", "Дэдпул 2"}, {"Гай Ричи", "Меч короля Артура"}]

# d = dict(directors)
# print(d)
#>>> {'Райан Джонсон': 'Звездные войны: Последний Джедай', 'Дэдпул 2': 'Дэвид Литч', 'Гай Ричи': 'Меч короля Артура'}

# print(d["Гай Ричи"])
#>>> Меч короля Артура
# print(d["James Cameron"])
# >>> KeyError: 'James Cameron'

#==========================================================================

"""
Проверка наличия значения в словаре посредством  in
"""
directors = [{"Райан Джонсон", "Звездные войны: Последний Джедай"},
{"Дэвид Литч", "Дэдпул 2"}, {"Гай Ричи", "Меч короля Артура"}]

# d = dict(directors)
#
# print("Дэвид Литч" in d)
# print("Дэвид Литч" not in d)
# print("James Cameron" in d)
# print("James Cameron" not in d)

#==========================================================================

"""
Обновление значений обращаясь по ключу
"""
# directors = [{"Райан Джонсон", "Звездные войны: Последний Джедай"},
# {"Дэвид Литч", "Дэдпул 2"}, {"Гай Ричи", "Меч короля Артура"}]
#
# d = dict(directors)
#
# d["Гай Ричи"] = "Карты, деньги, два ствола"
# print(d)
#
# d["James Cameron"] = "Avatar"
# print(d)

#==========================================================================

"""
Подсчет количества символов в строчке
"""

# s = "Строка, содержащая произвольный набор символов!"
#
# d = dict()
#
# for letter in s:
#     if letter not in d:
#         d[letter] = 1
#     else:
#         d[letter] +=1
#
# print(d)

"""
Данный способ самый быстрый. Быстрее чем get и default
"""

# >>> {'С': 1, 'т': 1, 'р': 4, 'о': 7, 'к': 1, 'а': 4, ',': 1, ' ': 4, 'с': 2, 'д': 1, 'е': 1, 'ж': 1, 'щ': 1, 'я': 1,
#  'п': 1, 'и': 2, 'з': 1, 'в': 3, 'л': 2, 'ь': 1, 'н': 2, 'ы': 1, 'й': 1, 'б': 1, 'м': 1, '!': 1}

#==========================================================================

"""
копирование и очистка
"""

# directors = [{"Райан Джонсон", "Звездные войны: Последний Джедай"},
# {"Дэвид Литч", "Дэдпул 2"}, {"Гай Ричи", "Меч короля Артура"}]
#
# d = dict(directors)
#
# a = d.copy()
# print(a)
#
# d.clear()
# print(d)
#==========================================================================

"""
Удаление элементов
"""

"""
удаление элемента
"""

# directors = [{"Райан Джонсон", "Звездные войны: Последний Джедай"},
# {"Дэвид Литч", "Дэдпул 2"}, {"Гай Ричи", "Меч короля Артура"}]
# d = dict(directors)
# a = d.copy()
#
# # del_item = a.popitem()
# # print(del_item)
#
"""
удаление по ключу
"""
#
# del_item = a.pop("Райан Джонсон", None)
# print(del_item)
#
# print(a)


#==========================================================================
"""
Обновление словаря
"""

# directors = [{"Райан Джонсон", "Звездные войны: Последний Джедай"},
# {"Дэвид Литч", "Дэдпул 2"}, {"Гай Ричи", "Меч короля Артура"}]
#
# d = dict(directors)
# print(d)
#
# d.update([("Джеймс Кэмерон", "Аватар"), ("Гай Ричи", "Карты, деньги, два ствола")])
# print(d)
#
# d.update({"Джеймс Кэмерон": "Титаник", "Роланд Эммерих": "День независимости"})
# print(d)

#==========================================================================

"""
Метод Get
Подсчет количества символов
"""

# directors = [{"Райан Джонсон", "Звездные войны: Последний Джедай"},
# {"Дэвид Литч", "Дэдпул 2"}, {"Гай Ричи", "Меч короля Артура"}]

# {'Звездные войны: Последний Джедай': 'Райан Джонсон', 'Дэвид Литч': 'Дэдпул 2', 'Меч короля Артура': 'Гай Ричи',
#  'Джеймс Кэмерон': 'Титаник', 'Гай Ричи': 'Карты, деньги, два ствола', 'Роланд Эммерих': 'День независимости'}

# s = "Строка, содержащая произвольный набор символов! "
# d = dict()
# for letters in s:
#     d[letters] = d.get(letters, 0) + 1
# print(d)

#==========================================================================

"""
Методы представления
"""
# directors = [{"Райан Джонсон", "Звездные войны: Последний Джедай"},
# {"Дэвид Литч", "Дэдпул 2"}, {"Гай Ричи", "Меч короля Артура"}]
#
# d = dict(directors)
#
# keys = d.keys()
# values = d.values()
# items = d.items()
# print(keys)
# print(values)
# print(items)
#
# d.update([("Джеймс Кэмерон", "Аватар"), ("Гай Ричи", "Карты, деньги, два ствола")])
#
# print(keys)
# print(values)
# print(items)

#==========================================================================


"""
Итерирование по словарю
"""

# directors = [("Райан Джонсон", "Звездные войны: Последний Джедай"),
#              ("Дэвид Литч", "Дэдпул 2"), ("Гай Ричи", "Меч короля Артура")]
#
#
# d = dict(directors)

# for el in d:
    # print(el, end=", ")
    # print(el, d[el],  end=", ")

# for el in d.keys():
    # print(el, end=", ")

# for el in d.values():
#     print(el, end=", ")

# for el in d.items():
    # print(el, end=", ")
# >>> ('Райан Джонсон', 'Звездные войны: Последний Джедай'), ('Дэвид Литч', 'Дэдпул 2'), ('Гай Ричи', 'Меч короля Артура')

# cnt = len(d)
# print(cnt)

#==========================================================================

directors = [("Райан Джонсон", "Звездные войны: Последний Джедай"),
             ("Дэвид Литч", "Дэдпул 2"), ("Гай Ричи", "Меч короля Артура")]

d = dict(directors)

# d = sorted(d.items())
# print(d)
# >>> [('Гай Ричи', 'Меч короля Артура'), ('Дэвид Литч', 'Дэдпул 2'),
# ('Райан Джонсон', 'Звездные войны: Последний Джедай')]


# d = dict(sorted(d.items())) # СОртировка по ключам
# print(d)

# >>> {'Гай Ричи': 'Меч короля Артура', 'Дэвид Литч': 'Дэдпул 2', 'Райан Джонсон': 'Звездные войны: Последний Джедай'}


# d = dict(sorted(d.items(), key = lambda x: x[1]))# Сортировка по значаения, поэтому надо указывать ключ для сравнения
# print(d)
# >>> {'Дэвид Литч': 'Дэдпул 2', 'Райан Джонсон': 'Звездные войны: Последний Джедай', 'Гай Ричи': 'Меч короля Артура'}

# d = dict(sorted(d.items(), key = lambda x: x[1], x[0]))# Сортировка по значению и если есть повторения сортировка по ключу
#  print(d)


#==========================================================================

"""
Ключами могут быть только неизменяемые данные:
- строки
- числа
- кортежи

Нельзя использовать список в качестве ключа, поскольку невозможно посчитать Хэш списка(тип данных изменяемых на лету).
Не рекомендуется использовать вещественные цифры , к примеру 1.0 или 1. 6

"""

# Пример ключ-кортеж
# cities = {
#     (55.75, 37.5): "Moscow",
#     (59.8, 30.3): "Saint-Petersburg",
#     (54.32, 40.29): "Ulyanovsk"
# }

# print(cities[(55.75, 37.5)])
# >>> Moscow

# cities[(53.2, 50.15)] = "Samara"
# print(cities)

# >>> {(55.75, 37.5): 'Moscow', (59.8, 30.3): 'Saint-Petersburg', (54.32, 40.29): 'Ulyanovsk', (53.2, 50.15): 'Samara'}

#======================================================================================================================

"""
Вложенные словари
"""

# films = {
#     "День независимости": {"year": 1996, "director": "Роланд Эммерих"},
#     "Дедпул 2": {"year": 2010, "director": "Дэвид Линч"}
# }
#
# # print(films["День независимости"]["year"])
# # >>> 1996
#
#
# def print_film(films, t=0):
#     for key, val in films.items():
#         print(" "*t + key + ":")
#         if isinstance(val, dict):
#             print(val, t + 4)
#         else:
#             print(" "*(t+4) + str(val))
#         # print()
#
# print_film(films)

#======================================================================================================================

"""
Дополнительные возможности стандартной библиотеки
"""


"""
Модуль Collections
"""

from collections import Counter, ChainMap, defaultdict

s = "Строка, содержащая произвольный набор симоволов!"
d = Counter(s)
# print(d)
# >>> Counter({'о': 8, 'р': 4, 'а': 4, ' ': 4, 'в': 3, 'с': 2, 'и': 2, 'л': 2, 'н': 2, 'С': 1, 'т': 1, 'к': 1, ',': 1,
# 'д': 1, 'е': 1, 'ж': 1, 'щ': 1, 'я': 1, 'п': 1, 'з': 1, 'ь': 1, 'ы': 1, 'й': 1, 'б': 1, 'м': 1, '!': 1})

# print(d['s'])
# >>> 0
# print(d['с'])
# >>> 2
# print('q' in d)
# >>> False


# print(list(d.elements()))
# >>> ['С', 'т', 'р', 'р', 'р', 'р', 'о', 'о', 'о', 'о', 'о', 'о', 'о', 'о', 'к', 'а', 'а', 'а', 'а', ',', ' ', ' ',
# ' ', ' ', 'с', 'с', 'д', 'е', 'ж', 'щ', 'я', 'п', 'и', 'и', 'з', 'в', 'в', 'в', 'л', 'л', 'ь', 'н', 'н', 'ы', 'й',
# 'б', 'м', '!']


# print(d.most_common(5))
# >>> [('о', 8), ('р', 4), ('а', 4), (' ', 4), ('в', 3)]


# print(d.most_common()[:-6:-1])
# >>> [('!', 1), ('м', 1), ('б', 1), ('й', 1), ('ы', 1)]


# print(Counter('abracadabra').most_common(1))
# >>> [('a', 5)]




s = "Строка, содержащая произвольный набор симоволов!"
# d = defaultdict(int)
#
# for letters in s:
#     d[letters] +=1
# print(d)

# >>> defaultdict(<class 'int'>, {'С': 1, 'т': 1, 'р': 4, 'о': 8, 'к': 1, 'а': 4, ',': 1, ' ': 4, 'с': 2, 'д': 1,
# 'е': 1, 'ж': 1, 'щ': 1, 'я': 1, 'п': 1, 'и': 2, 'з': 1, 'в': 3, 'л': 2, 'ь': 1, 'н': 2, 'ы': 1, 'й': 1, 'б': 1,
# 'м': 1, '!': 1})


"""
ChainMap - это класс, который дает возможность объединить несколько сопоставлений вместе, таким образом, чтобы они стали
единым целым
"""


car_parts = {
    'hood': 500,
    'engine': 5000,
    'front_door': 750
}


car_options = {
    'A/C': 1000,
    'Turbo': 2500,
    'rollbar': 300
}

car_accessories = {
    'cover': 100,
    'hood_ornament': 150,
    'seat_cover': 99
}

car_parts2 = {
    'hood': 1500,
    'engine': 4000,
    'front_door': 500
}


car_pricing = ChainMap(car_accessories, car_options, car_parts, car_parts2)


















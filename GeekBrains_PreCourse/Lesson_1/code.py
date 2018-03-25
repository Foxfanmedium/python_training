# Python.org - 3 версия
# PyCharm Community - JetBrains
# Ctrl (Command) + Alt + L  форматирование кода
# Ctrl (Command) + /
# НЕ ДЕЛАТЬ ДЗ В МЕТОДИЧКЕ
# НЕ ДЕЛАТЬ ДЗ ПО КНОПКЕ НА САЙТЕ "ДОМАШНЕЕ ЗАДАНИЕ"
# pastebin.com
# ДЗ в архиве (тип не важен), 3 файла: easy.py, normal.py.py, hard.py


age = 30  # int
name = 'Bob'  # str
money = 200.10  # float
is_admin = False
is_god = True
accounts = [2, 10, 'Bob', is_admin, money]  # list
accounts_tuple = (2, 10, 'Bob', is_admin, money)  # tuple
bank_accounts = {'Alice': 200.10, 'Bob': 100.10}  # dict

# age = 'qyw'
# print(age + 10)
# print(age - 10)
# print(age * 10)
# print(age / 10)
# print(age // 10)
# # 5 // 2 = 2
# print(age % 2)
# # 5 % 2 = 1
# print(age ** 2)
# print('Hello', name)

# name = input('Input name:')
# print('Hello', name)

# int(arg)
# str(arg)
# float(arg)
# bool(arg)

# age = int(input('Input age:'))
# print(age + 10)
#
# print(age > 18)
# print(age < 30)
# print(age == 34)
# print(age != 39)
# print(age >= 39)
# print(age <= 39)

# age = 36
# is_god = False
#
# if 10 < age < 35 or is_god:
#     print('Вы не в зоне риска')
# elif age < 40:
#     print('Вы молоды, но за здоровьем следите!')
# else:
#     print('Вы в зоне риска!')

counter = 10

while counter > 0:

    if counter % 2 == 0:
        counter -= 1
        continue

    print(counter)
    # counter = counter - 1
    counter -= 1

    # if counter == 2:
    #     break
else:
    print('Цикл завершен корректно!')

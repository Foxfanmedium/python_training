# print('Hello' + 'world')
# print('Hello' ' ' 'world')
# print('Hello ' * 3)
#
# email = 'test@mail.com'
# index = email.find('@')
# print(email[index+1:])
#
# print(email[4])
# print(email[-1])
# print(email[0:4])
# print(email[4:])
# print(email[0::2])
# print(email[::-1])
# print(len(email))

# name = 'ивАн пЕтРов пЕ'
# print(name.title())
# print(name.capitalize())
# print(name.upper())
# print(name.lower())
# print(name.find('пЕ', 6))
#
# name = 'Иван'
# surname = 'Петров'
# age = 20
# print('Приветствую тебя - ' + name + ' ' + surname + ', которому ' + str(age) + ' лет')
# print('Приветствую тебя - %s %s, которому %i лет' % (name, surname, age))
# print('Приветствую тебя - {} {}, которому {} лет'.format(name, surname, age))
# print(f'Приветствую тебя - {name} {surname}, которому {age} лет')

# peoples = ['Bob', 'Alice', 'Jack']
# print(peoples[0])
# print(peoples[1:])
# print(peoples[-1])
# print(peoples + ['Olga', 'Oleg'])
# new_peoples = peoples + ['Olga', 'Oleg']
# print(new_peoples, len(new_peoples))
# print(len(peoples))
# print(peoples.index('Alice'))
# print(peoples.pop())
# print(peoples)
# peoples.insert(0, 'Alex')
# print(peoples)
# peoples.append('Oleg')
# print(peoples)
# peoples[0] = 'qwerty'
# print(peoples)
#
# print('Oleg2' in peoples)
#
# x = [1, 2, 3, 4, [5, 6, 7, 8, [9, 10, 11]]]
# print(x[4][4][1])


# my_tuple = (1, 2, 3, 4)
# print(my_tuple[1:])
# print(my_tuple[-1])
# my_tuple[0] = 100

# peoples = ['Alex', 'Bob', 'Alice']

# i = 0
# while i < len(peoples):
#     print(peoples[i])
#     i += 1

# for name in peoples:
#     print(name)

# bank_accounts = {'Alice': 200.10, 'Bob': 100.20, 'Alex': 300}
# print(bank_accounts)
# print(bank_accounts['Alice'])
# bank_accounts['Alex'] = 150.10
# print(bank_accounts.pop('Alice'))
# print(bank_accounts)
# print(bank_accounts.popitem())
# print(bank_accounts)

# for name in bank_accounts.keys():
#     print(name)
#
# for money in bank_accounts.values():
#     print(money)
#
# for name, money in bank_accounts.items():
#     print(name, money)

# https://pythonworld.ru/tipy-dannyx-v-python/stroki-funkcii-i-metody-strok.html
# https://pythonworld.ru/tipy-dannyx-v-python/spiski-list-funkcii-i-metody-spiskov.html
# https://pythonworld.ru/tipy-dannyx-v-python/slovari-dict-funkcii-i-metody-slovarej.html


x = [1, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7]
y = [6, 6, 7, 7, 8, 8, 9, 9]


some_set = set(x)
some_set2 = set(y)
# print(some_set)
#
# print(set('hellllllo'))
# print(7 in some_set)

print(some_set)
print(some_set2)

print(some_set - some_set2)
print(some_set & some_set2)
print(some_set | some_set2)
print(some_set ^ some_set2)



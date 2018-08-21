"""
На этой неделе мы с вами реализуем собственный key-value storage. Вашей задачей будет написать скрипт,
который принимает в качестве аргументов ключи и значения и выводит информацию из хранилища (в нашем случае — из файла).
Запись значения по ключу
> storage.py --key key_name --val value
Получение значения по ключу
> storage.py --key key_name
Ответом в данном случае будет вывод с помощью print соответствующего значения
> value
или
> value_1, value_2
если значений по этому ключу было записано несколько. Обратите внимание на пробел после запятой.
Если значений по ключу не было найдено, выводите пустую строку или None.
Для работы с аргументами командной строки используйте модуль argparse. Вашей задачей будет считать аргументы,
переданные вашей программе, и записать соответствующую пару ключ-значение в файл хранилища или вывести значения,
если был передан только ключ. Хранить данные вы можете в формате JSON с помощью стандартного модуля json.
Файл следует создавать с помощью модуля tempfile.
import os
import tempfile
storage_filename = os.path.join(tempfile.gettempdir(), 'storage.data')
with open(storage_filename, 'w') as f:
  ...
Создайте скрипт хранилища и загрузите его на платформу.
"""

import sys
import os
import tempfile

key_name = sys.argv[2]
if len(sys.argv) > 3:
    value_name = sys.argv[4]
else:
    value_name = None

storage_filename = os.path.join(tempfile.gettempdir(), 'storage.data')
if not os.path.exists(storage_filename):
    open(storage_filename, 'w').close()

if value_name is not None:
    with open(storage_filename, 'a') as f:
        f.write(key_name + ' ' + value_name + '\n')
else:
    answer = ''
    with open(storage_filename, 'r') as f:
        storage = f.readlines()
        for string in storage:
            pair = string.split()
            if pair[0] == key_name:
                answer = answer + pair[1] + ', '
    if answer:
        print(answer[:-2])
    else:
        print(None)

"""Решение
Поздравляем с первой полноценной программой на Python в рамках нашего курса! Она была заметно сложнее предыдущих и 
помогла вам разобраться сразу с несколькими моментами. Хорошим подходом было бы разбить свою программу на
 функции — обратите внимание, все команды вынесены в отдельные функции, а get_data мы переиспользуем 
 в нескольких местах. Ключевым моментом в разработке любого приложения является выбор подходящей структуры данных. 
 В этом примере логичным вариантом было использовать словарь, потому что он по сути и является key-value хранилищем, 
 а значения просто хранить в списке.
Также в этом задании мы использовали модуль argparse для считывания аргументов командной строки и json для хранения 
данных в файле. Самым простым подходом было просто перечитывать при каждом обращении файл, преобразуя его в словарь, 
добавляя значения при необходимости. Модуль os помогает нам в проверке существования файла хранилища при первом 
запуске программы. В Python богатая стандартная библиотека, очень важно представлять себе, какие модули помогут 
нам в решении наших задач, и уметь быстро разбираться в документации к новым функциям.
Обратите внимание, в примере мы для простоты используем глобальную переменную, однако в реальном приложении вы, 
скорее всего, написали бы для решения похожей задачи свой класс и инкапсулировали бы в нём информацию о хранилище 
и его методы. В следующей неделе мы разберем объектно-ориентированный подход и его плюсы.
"""

import argparse
import json
import os
import tempfile


storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')


def clear():
    os.remove(storage_path)


def get_data():
    if not os.path.exists(storage_path):
        return {}
    with open(storage_path, 'r') as f:
        raw_data = f.read()
        if raw_data:
            return json.loads(raw_data)
        return {}


def put(key, value):
    data = get_data()
    if key in data:
        data[key].append(value)
    else:
        data[key] = [value]
    with open(storage_path, 'w') as f:
        f.write(json.dumps(data))


def get(key):
    data = get_data()
    return data.get(key)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--key', help='Key')
    parser.add_argument('--val', help='Value')
    parser.add_argument('--clear', action='store_true', help='Clear')
    args = parser.parse_args()
    if args.clear:
        clear()
    elif args.key and args.val:
        put(args.key, args.val)
    elif args.key:
        print(get(args.key))
    else:
        print('Wrong command')

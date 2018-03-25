# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

# import os
# import sys
#
# under = '_'

# try:
#     for i in range(1, 10):
#         dir_path = under.join(['dir', str(i)])
#         os.mkdir(dir_path)
# except FileExistsError:
#     print("Такая директория уже существует")


# for i in range(1, 10):
#     dir_path = under.join(['dir', str(i)])
#     os.rmdir(dir_path)

# Почему в Windows для запуска метода os.remove возвращает ошибку "Отказанов  доступе"? Как это обойти?

# ======================================================================================================================
# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.
import os


def current_directory():
    current_directory = os.getcwd()
    for name in os.listdir(current_directory):
        print(name)

# ======================================================================================================================
# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

# import shutil
# shutil.copy('easy.py','hw05_easy_copy.py')



"""
Создание/вызов процесса в всистем производится при помощи
системного вызова fork

Вывод доступных аттрибутов для модуля OS
print(dir(os))

В Windows fork недоступен для использования

Вывод всех процессов
$ ls -l

Поиск процессов по имени процесса
$ ps uax| grep ex.p

"""

# import time
# import os
#
# pid = os.fork()
#
#
# if pid == 0:
#     # inherit process
#     while True:
#         print('chile', os.getpid())
#         time.sleep(5)
#
# else:
#     # parent process
#     print('parent', os.getpid())
#     os.wait()


#====================================================================================================================

"""
Файлы в родительском и дочернем процессах
"""

# import os
#
# f = open('data.txt')
# foo = f.readline()
#
# if os.fork == 0:
#     # inherit process
#     foo = f.readline()
#     print('child', foo)
# else:
#     # parent process
#     foo = f.readline()
#     print('parent', foo)

#====================================================================================================================
"""
Создание процесса, модуль multiprocessing
"""

from multiprocessing import Process


# def f(name):
#     print('hello', name)
#
#
# p = Process(target =f, args = ("Bob", ))
# p.start()
# p.join()


# Альтернативный спсооб создания процесса

class PrintProcess(Process):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        print('hello', self.name)


p = PrintProcess('Mike')
p.start()
p.join()



















#print("Hello, programmer!")
#print("Hello!")
#input()
#=======================================================================================================================
 #coding: utf-8
import os
import psutil #pip install psutil

answer = input("Давайте поработаем? (Y/N)")
if answer == 'Y':
    print("Отлично хозяин!")
    print("Я умею:")
    print("[1] - выведу список файлов")
    print("[2] - выведу информацию о системе")
    print("[3] - выведу список процессов")
    do = int(input("Укажите номер действия:"))

    if do == 1:
         print(os.listdir())
    elif do == 2:
        pass
    elif do == 3:
        print(psutil.pids())
    else:
        pass













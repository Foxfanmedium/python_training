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

# type(do) - display information about object
# type("") or type('') - name of object like a string type
# import os - import module 'os'
# os.listdir() - show all files in current directory
# import psutil - import module psutil, pay attention this module is third-party application
# pip - manager for instalation packages
# pip install psutil - install module psutil
# dir(psutil) - show module content
# help(psutil) - display all information about module
#
#










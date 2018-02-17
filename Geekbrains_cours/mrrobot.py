#print("Hello, programmer!")
#print("Hello!")
#input()
#=======================================================================================================================
 #coding: utf-8
#import os
#import sys
#import psutil

#answer = input("Давайте поработаем? (Y/N)")
#if answer == 'Y':
#    print("Отлично хозяин!")
#    print("Я умею:")
 #   print("[1] - выведу список файлов")
 #   print("[2] - выведу информацию о системе")
 #   print("[3] - выведу список процессов")
 #   do = int(input("Укажите номер действия:"))
#
#    if do == 1:
#        print(os.listdir())
#    elif do == 2:
#        print('Ваша ОС: ' + sys.platform + os.name)
#        print('Кодировка вашей ОС: ' + sys.getfilesystemencoding())
#        print('Вы авторизованы в системе как : ' + os.getlogin())
#        print('Текущая директория : ' + os.getcwd())
 #       print('Версия установленого Python : ' + sys.version)
 #       #print('Количество поцессоров на вашей машине : ' + psutil.cpu_count())
 #   elif do == 3:
 #       pass
        #print(psutil.pids())
 #   else:
  #      pass

# type(do) - display information about object
# type("") or type('') - name of object like a string type
# import os - import module 'os'
# os.listdir() - show all files in current directory
# import psutil - import module psutil, pay attention this module is third-party application
# pip - manager for instalation packages
# pip install psutil - install module psutil
# dir(psutil) - show module content
# help(psutil) - display all information about module
# pip install psutil

#=======================================================================================================================
 #WHILE
 #coding: utf-8
import os
import sys
import shutil
#import psutil

#print('Great Python Program!')
#print('Hello, programmer!')
#name = input('Your name is: ')

#print(name, 'welcome to the Python world!')
#PEP8

#answer = ''
#while answer != 'q':
#    answer = input("Давайте поработаем? (Y/N/q)")
#    if answer == 'Y':
#        print("Отлично хозяин!")
#        print("Я умею:")
#        print("[1] - выведу список файлов")
#        print("[2] - выведу информацию о системе")
#        print("[3] - выведу список процессов")
#        print("[4] - coping all files in current directory")
#        print("[5] - coping pointed file")
#        do = int(input("Укажите номер действия:"))

#        if do == 1:
#            print(os.listdir())
#        elif do == 2:
#            print('Ваша ОС: ' + sys.platform + os.name)
#            print('Кодировка вашей ОС: ' + sys.getfilesystemencoding())
#            print('Вы авторизованы в системе как : ' + os.getlogin())
#            print('Текущая директория : ' + os.getcwd())
#            print('Версия установленого Python : ' + sys.version)
            #print('Количество поцессоров на вашей машине : ' + psutil.cpu_count())
#        elif do == 3:
#            pass
            #print(psutil.pids())
#        elif do == 4:
#            print ('Duplicating all files in current directory')
            #file_list = os.listdir()
            #i = 0
            #while i < file_list[]:
            #    newfile = file_list[i] + '.dupl'
            #   shutil.copy(file_list[i], newfile)   # coping all files in current directory
            #    print (file_list[i] + '.dupl')
            #    i+=1

# My version of answer:
 #       elif do == 5:
  #          print(os.listdir())
  #          file_list = os.listdir()
  #          number = int(input("Point a number of file which you wish to copy:"))
   #         i = number - 1
   #         new_file = file_list[i] + '.dupl'
   #         for i in file_list[i]:
     #           shutil.copy(file_list[i], new_file)
    #        print(new_file)


 #       else:
 #           pass


#=======================================================================================================================
import os
import sys
import shutil
#import psutil

def duplicate_file(filename):
    if os.path.isfile(filename):
        newfile = filename + '.dupl'
        shutil.copy(filename, newfile)
        if os.path.exists(newfile):        # function of checking if file is existed
            print("File", newfile, "is created")
            return True
        else:
            print("Some problems were appeared")
            return False

def double_files(dirname):
    i = 0
    while i < len(file_list(dirname)):
        duplicate_file(file_list[i])
        i += 1

def random_delete(dirname):
    file_list = os.listdir(dirname)
    if file_list:
        i = random.randrange(0, len(file_list))
        fullname= os.path.join(dirname, file_list[i])
        if os.path.isfile(fullname):
            os.remove(fullname)
            print("The file", fullname, "is deleted")

def sys_info():
    print('Ваша ОС: ' + sys.platform + os.name)
    print('Кодировка вашей ОС: ' + sys.getfilesystemencoding())
    print('Вы авторизованы в системе как : ' + os.getlogin())
    print('Текущая директория : ' + os.getcwd())
    print('Версия установленого Python : ' + sys.version)

def del_duplicate(dirname):
    file_list = os.listdir(dirname)
    doubl_count = 0
    for f in file_list:
        fullname = os.path.join(dirname, file_list[i])  # join operation - for join dir and name of file
        if fullname.endswith('.dupl'):
            os.remove(fullname)  # remove operation
            if not os.path.exists(fullname):
                doubl_count += 1
                print("File", fullname, "was deleted")
    return doubl_count


def main():
    print('Great Python Program!')
    print('Hello, programmer!')
    name = input('Your name is: ')

    print(name, 'welcome to the Python world!')
    #PEP8

    answer = ''
    while answer != 'q':
        answer = input("Давайте поработаем? (Y/N/q)")
        if answer == 'Y':
            print("Отлично хозяин!")
            print("Я умею:")
            print("[1] - выведу список файлов")
            print("[2] - выведу информацию о системе")
            print("[3] - выведу список процессов")
            print("[4] - coping all files in current directory")
            print("[5] - coping pointed file")
            print("[6] - remove duplicates")
            print("[7] - remove random file")
            do = int(input("Укажите номер действия:"))

            if do == 1:
                print(os.listdir())
            elif do == 2:
                sys_info()
            elif do == 3:
                pass
                #print(psutil.pids())
            elif do == 4:
                print('Duplicating all files in current directory')
                double_files('.')

            elif do == 5:
                print('Duplicating the pointed file')
                filename = input("Point name of file")
                duplicate_file(filename)

            elif do == 6:
                print('Duplicating all files in current directory')
                dirname = input("Point directory")
                count = del_duplicate(dirname)
                print("-- Deleted files:", count)

            elif do == 6:
                print('Deleting random file')
                dirname = input("Point directory")
                random_delete(dirname)

            else:
                pass
        elif answer == 'N':
            print("Good buy!")
        else:
            print("Unknown format")

if __name__=="__main__":
    main()

import sys
import os
print(sys.argv)

name = sys.argv[1]
print(name.title())

name = sys.argv[1]
try:
    create_folder = os.mkdir(name)
except FileExistsError:
    print('Указанная папка уже существует')
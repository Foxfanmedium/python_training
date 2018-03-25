from random import randrange
from random import randint
import random
# для генерации 3-х строк первая строка будет for i in range(3)

sorted_list_1 = []
while len(sorted_list_1) < 9:
    i = randrange(1, 91)
    if i in sorted_list_1:
        pass
    else:
        sorted_list_1.append(i)
    sorted_list_1 = sorted(sorted_list_1)
print(sorted_list_1)

sorted_list_2 = []
while len(sorted_list_2) < 9:
    i = randrange(1, 91)
    if i in (sorted_list_2 or sorted_list_1):
        pass
    else:
        sorted_list_2.append(i)
sorted_list_2 = sorted(sorted_list_2)
print(sorted_list_2)

sorted_list_3 = []
while len(sorted_list_3) < 9:
    i = randrange(1, 91)
    if i in (sorted_list_3 or sorted_list_2 or sorted_list_1):
        pass
    else:
        sorted_list_3.append(i)
sorted_list_3 = sorted(sorted_list_3)
print(sorted_list_3)












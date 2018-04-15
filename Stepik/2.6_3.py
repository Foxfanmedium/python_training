"""
Напишите программу, которая считывает список чисел lst из первой строки и число x из второй строки,
которая выводит все позиции, на которых встречается число x в переданном списке lst.
Позиции нумеруются с нуля, если число x не встречается в списке, вывести строку "Отсутствует"
(без кавычек, с большой буквы).
Позиции должны быть выведены в одну строку, по возрастанию абсолютного значения.
"""

#lst1 = [input('')]
lst = [int(i) for i in input().split()]
n = int(input())
new_list = []

if n in lst:
    for i in range(0, len(lst)):
        if lst[i] == n:
            new_list.append(i)
else:
    print('Отсутствует')
new_list = [str(a) for a in new_list]
print(" ".join(new_list))
#=====================================================================================================================
# l = [int(i) for i in input().split()]
# x = int(input())
# if not x in l: print('Отсутствует')
# for i in range(len(l)):
#     if l[i]==x: print(i, end = ' ')
#=====================================================================================================================
# numbers = [int(i) for i in input().split()]
# needed = int(input())
# if needed not in numbers:
#     print("Отсутствует")
# else:
#     [print(i, end=" ") for i, x in enumerate(numbers) if x == needed]






















# Задание - 1
# Создайте функцию, принимающую на вход Имя, возраст и город проживания человека
# Функция должна возвращать строку вида "Василий, 21 год(а), проживает в городе Москва"

#
# def inf_people(name, age, city, *args):
#     name = input('Input your name: ').title()
#     age = int(input('Input your age: '))
#     city = input('Input your city: ').title()
#     print(name, age, 'год(а)', 'проживает в городе', city)
#
#
# inf_people(1, 2, 3)

#Ответ от преподавателя

# def person_render(name, age, town):
#     return '{}, {} год(а), проживает в городе {}'.format(name, age, town)
#
# print(person_render('Rail', '32', 'Kazan'))

#=======================================================================================================================
# Задание - 2
# Создайте функцию, принимающую на вход 3 числа, и возвращающую наибольшее из них

# first = int(input())
# second = int(input())
# third = int(input())
# print(max(first, second, third))


# value = input()
# for_print = value.split(' ')
# max_list = max(for_print)
# min_list = min(for_print)
#
# print(for_print)
# print(max_list)
# print(min_list)

#Ответ от преподавателя

# def max_number(a,b,c):
#     return max(a,b,c)
#
# print(max_number(5,2,500))

#=======================================================================================================================
# Задание - 3
# Создайте функцию, принимающую неограниченное количество строковых аргументов,
# верните самую длинную строку из полученных аргументов
#
# inp = input('Enter several arguments:')
# split_inp = max(inp.split(), key=len)
# print(split_inp)

# Как сделать тоже самое с циклом for?


#Ответ от преподавателя


def max_string(*args):
    return max(args, key=len)

print(max_string('jhsavsdhvljkasdv', 'qwerty', 'hsjknfdskj'))








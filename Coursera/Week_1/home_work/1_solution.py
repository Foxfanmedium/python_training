"""Вы должны создать Python модуль 1_solution.py и загрузить его на платформу – этот файл мы запустим с
аргументом командной строки – строкой, состоящей из цифр. Например, вот такой:
“873”
Чтобы получить ввод, вы в начале программы можете считать его, используя модуль стандартной библиотеки sys:
import sys
digit_string = sys.argv[1]

В переменной digit_string будет содержаться строка “873” (ну или какая-то другая строка, сгенерированная нами,
в том числе другой длины). В строке, подаваемой на вход, будут только символы, соответствующие цифрам от 0 до 9.
В результате ваша программа должна напечатать на экран сумму цифр (для строки “873” сумма будет 18).
То, что полученная программа ведет себя должным образом можно проверить локально, запустив ее следующим образом:
python3 1_solution.py 873

В списке sys.argv будут лежать аргументы командной строки, sys.argv[0] - имя запущенного файла, sys.argv[1] - строка,
сумму цифр которой необходимо посчитать и вывести на экран"""

import sys


def solution(digit_string):
    # digit_string = str(input())
    digit_string = sys.argv[1]
    list_num = list(map(int, digit_string))
    return sum(list_num)


if __name__ == "__main__":
    solution(sys.argv[1])
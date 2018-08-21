import random

number = random.randint(0, 101)

while True:

    your_number = input('Введите число: ')
    if not your_number or your_number == "exit":
        break

    if not your_number.isdigit():
        print("Введите правильное число")
        continue
    your_number = int(your_number)

    if your_number > number:
        print("Загаданное число меньше")
    elif your_number < number:
        print("Загаданное число больше")
    else:
        print("Совершенно верно!")
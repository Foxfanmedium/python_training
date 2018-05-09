#======================================================================================================================
import random
# number = 42
number = random.randint(0, 50)

while True:
    answer = input("Введите ваше число: ")
    if not answer or answer == "exit":
        break

    if not answer.isdigit():
        print("введите правильное число")
        continue

    user_answer = int(answer)

    if user_answer > number:
        print("Загаданное число меньше")
    elif user_answer< number:
        print("Загаданное число больше")
    else:
        print("Совершенно верно!")
        break









